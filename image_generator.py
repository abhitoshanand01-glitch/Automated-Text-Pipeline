import os
import textwrap
from PIL import Image, ImageDraw, ImageFont

def create_poetry_image(meta, poem_lines):
    # 1. Canvas aur background setup
    img_w, img_h = 1080, 1080
    img = Image.new('RGB', (img_w, img_h), color=(25, 25, 30))
    draw = ImageDraw.Draw(img)
    
    # 2. Font setup
    try:
        font_title = ImageFont.truetype("nirmala.ttf", 60)
        font_text = ImageFont.truetype("nirmala.ttf", 40)
        font_watermark = ImageFont.truetype("nirmala.ttf", 30)
    except:
        font_title = font_text = font_watermark = ImageFont.load_default()

    # 3. ✨ NAYA LOGIC: Text Wrapping ✨
    max_chars = 45 # Ek line mein lagbhag 45 characters aayenge (canvas width ke hisaab se)
    wrapped_poem = []
    
    for line in poem_lines:
        if line.strip() == "":
            wrapped_poem.append("")
        else:
            # textwrap lambe paragraph ko choti lines mein tod dega
            wrapped_lines = textwrap.wrap(line, width=max_chars)
            wrapped_poem.extend(wrapped_lines)

    # 4. Draw Title
    title = meta.get('TITLE', 'No Title')
    draw.text((100, 150), title, font=font_title, fill=(255, 215, 0)) # Yellow title
    
    # 5. Draw Body Text (Wrapped)
    y_text = 280 # Yahan se text shuru hoga
    for line in wrapped_poem:
        draw.text((100, y_text), line, font=font_text, fill=(230, 230, 230))
        y_text += 60 # Har line ke beech ka gap
        
    # 6. Draw Watermark
    author = meta.get('AUTHOR', 'Unknown')
    watermark = f"© {author} | Automated Publishing"
    draw.text((100, 950), watermark, font=font_watermark, fill=(150, 150, 150))
    
    # 7. Save Image
    os.makedirs("output_social", exist_ok=True)
    img.save(os.path.join("output_social", "kavita_post.png"))