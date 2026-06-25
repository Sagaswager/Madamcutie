cat > api/save-content.js << 'EOF'
export default async function handler(req, res) {
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');
  
  if (req.method === 'OPTIONS') return res.status(200).end();
  if (req.method !== 'POST') return res.status(405).end();

  const { filePath, content } = req.body;

  try {
    const getFile = await fetch(
      `https://api.github.com/repos/${process.env.GITHUB_REPO}/contents/${filePath}`,
      { headers: { Authorization: `Bearer ${process.env.GITHUB_TOKEN}` } }
    );
    const fileData = await getFile.json();
    
    const update = await fetch(
      `https://api.github.com/repos/${process.env.GITHUB_REPO}/contents/${filePath}`,
      {
        method: 'PUT',
        headers: {
          Authorization: `Bearer ${process.env.GITHUB_TOKEN}`,
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          message: 'Admin panel update',
          content: Buffer.from(content).toString('base64'),
          sha: fileData.sha,
        })
      }
    );

    if (update.ok) {
      res.json({ success: true });
    } else {
      res.status(500).json({ success: false });
    }
  } catch (e) {
    res.status(500).json({ success: false, error: e.message });
  }
}
EOF