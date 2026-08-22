import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Extract 'Neden Biz' section
neden_biz_pattern = re.compile(r'<!-- 7\. Neden Biz\? Section -->.*?</section>', re.DOTALL)
match = neden_biz_pattern.search(content)
if match:
    neden_biz_html = match.group(0)
    # Remove it from current location
    content = content.replace(neden_biz_html, '')
    
    # Update section number in comment
    neden_biz_html = neden_biz_html.replace('<!-- 7. Neden Biz?', '<!-- 6. Neden Biz?')
    
    # Insert it before <!-- 6. Testimonials Section -->
    target_pattern = '<!-- 6. Testimonials Section -->'
    content = content.replace(target_pattern, neden_biz_html + '\n\n' + target_pattern.replace('<!-- 6.', '<!-- 7.'))

# 2. Add h-full flex flex-col justify-center to the scroll-stack-cards
card_pattern = r'(class="scroll-stack-card [^"]+)(?=")'
def add_classes(m):
    classes = m.group(1)
    if 'h-full' not in classes:
        classes += ' h-full flex flex-col justify-center'
    return classes

content = re.sub(card_pattern, add_classes, content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print('Done!')
