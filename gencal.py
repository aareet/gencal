import datetime
from reportlab.lib.pagesizes import letter, landscape
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch

# Define start and end dates
start_date = datetime.date(2025, 10, 28)
end_date = start_date + datetime.timedelta(days=29)

# Create PDF
file_path = "30_day_calendar.pdf"
c = canvas.Canvas(file_path, pagesize=landscape(letter))

# Page setup
width, height = landscape(letter)
margin = 0.5 * inch
usable_width = width - 2 * margin
usable_height = height - 2 * margin

# Title
c.setFont("Helvetica-Bold", 18)
c.drawCentredString(width / 2, height - margin / 2,
                    f"30-Day Calendar: {start_date} to {end_date}")

# Grid setup
cols = 7
rows = 5
cell_width = usable_width / cols
cell_height = usable_height / rows

# Draw grid and fill dates
current_date = start_date
for row in range(rows):
    for col in range(cols):
        x = margin + col * cell_width
        y = height - margin - (row + 1) * cell_height
        c.rect(x, y, cell_width, cell_height)
        if current_date <= end_date:
            c.setFont("Helvetica", 10)
            c.drawString(x + 5, y + cell_height - 15, current_date.strftime("%b %d"))
            current_date += datetime.timedelta(days=1)

c.save()
print(f"Calendar saved to: {file_path}")

