import re

shop_file = r"c:\Users\Dell\Desktop\Saurabh\shop.html"

with open(shop_file, 'r', encoding='utf-8') as f:
    shop_content = f.read()

pagination_html = """
            </div>
            
            <div class="pagination-container" style="display: flex; justify-content: center; gap: 10px; margin-top: 50px; margin-bottom: 50px;">
                <button onclick="changePage(-1, true)" style="padding: 10px 20px; border: none; background: #f8f6f0; font-weight: 600; cursor: pointer; letter-spacing: 1px;">&lt; PREV</button>
                <button onclick="goToPage(1)" class="page-btn page-btn-1" style="padding: 10px 20px; border: 1px solid #111; background: #111; color: white; font-weight: 600; cursor: pointer;">1</button>
                <button onclick="goToPage(2)" class="page-btn page-btn-2" style="padding: 10px 20px; border: 1px solid #111; background: #fff; color: #111; font-weight: 600; cursor: pointer;">2</button>
                <button onclick="goToPage(3)" class="page-btn page-btn-3" style="padding: 10px 20px; border: 1px solid #111; background: #fff; color: #111; font-weight: 600; cursor: pointer;">3</button>
                <button onclick="changePage(1, true)" style="padding: 10px 20px; border: none; background: #f8f6f0; font-weight: 600; cursor: pointer; letter-spacing: 1px;">NEXT &gt;</button>
            </div>
            
            <script>
                let currentPage = 1;
                const totalPages = 3;
                
                function goToPage(page) {
                    if (page < 1 || page > totalPages) return;
                    currentPage = page;
                    
                    document.querySelectorAll('.page-item').forEach(el => el.style.display = 'none');
                    document.querySelectorAll('.page-' + page).forEach(el => el.style.display = 'block');
                    
                    document.querySelectorAll('.page-btn').forEach(btn => {
                        btn.style.background = '#fff';
                        btn.style.color = '#111';
                    });
                    const activeBtn = document.querySelector('.page-btn-' + page);
                    if (activeBtn) {
                        activeBtn.style.background = '#111';
                        activeBtn.style.color = 'white';
                    }
                    
                    window.scrollTo({top: document.querySelector('.grid-3').offsetTop - 100, behavior: 'smooth'});
                }
                
                function changePage(delta) {
                    goToPage(currentPage + delta);
                }
            </script>
"""

# We know the main grid is followed by the footer. 
# Let's just find "<!-- Footer -->" and put our code before it, but we also need to close the main section.
# Actually, the 48th card has "</div>\n</div>\n" then probably "</div>\n</div>\n</section>".
# Let's just replace '<!-- Footer -->' with the pagination and '<!-- Footer -->'.
# Wait, if we put pagination right before Footer, it will be outside the section?
# Let's insert it before the closing </section> tag that comes before the footer.
# But I am not sure if there is a </section> tag.

# I'll just use the easiest approach:
if "pagination-container" not in shop_content:
    shop_content = shop_content.replace('<!-- Footer -->', pagination_html + '\n\n    <!-- Footer -->')
    with open(shop_file, 'w', encoding='utf-8') as f:
        f.write(shop_content)
    print("Pagination added.")
else:
    print("Pagination already exists.")
