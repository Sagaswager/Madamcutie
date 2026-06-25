const https = require('https');

module.exports = async function(req, res) {
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'POST, OPTIONS');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');
  
  if (req.method === 'OPTIONS') return res.status(200).end();
  if (req.method !== 'POST') return res.status(405).end();

  const { fileName, fileContent } = req.body;

  try {
    const filePath = `assets/images/madam/${fileName}`;
    
    // Check if file already exists to get SHA
    let sha = undefined;
    try {
      const getRes = await fetch(
        `https://api.github.com/repos/${process.env.GITHUB_REPO}/contents/${filePath}`,
        { headers: { Authorization: `Bearer ${process.env.GITHUB_TOKEN}`, 'User-Agent': 'madamcutie-admin' } }
      );
      if (getRes.ok) {
        const existing = await getRes.json();
        sha = existing.sha;
      }
    } catch(e) {}

    const body = {
      message: 'Admin: Upload new image',
      content: fileContent,
      ...(sha && { sha })
    };

    const updateRes = await fetch(
      `https://api.github.com/repos/${process.env.GITHUB_REPO}/contents/${filePath}`,
      {
        method: 'PUT',
        headers: {
          Authorization: `Bearer ${process.env.GITHUB_TOKEN}`,
          'Content-Type': 'application/json',
          'User-Agent': 'madamcutie-admin'
        },
        body: JSON.stringify(body)
      }
    );

    if (updateRes.ok) {
      res.json({ success: true, path: `/${filePath}` });
    } else {
      const err = await updateRes.json();
      res.status(500).json({ success: false, error: err });
    }
  } catch (e) {
    res.status(500).json({ success: false, error: e.message });
  }
}
