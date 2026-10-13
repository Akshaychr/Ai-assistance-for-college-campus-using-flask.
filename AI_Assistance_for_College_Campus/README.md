# Soundarya Institute of Management and Science — Campus Assistant

A Flask-based campus help desk for Soundarya Institute of Management and Science, with a responsive chat interface and a starter knowledge base of common student, staff, and visitor questions. It runs locally and does not require an external AI API: questions are matched to relevant answers in `faq_data.py`.

## Included topics

Admissions and enrollment, academics, fees and financial aid, campus services, library, canteen, programs, events, housing and transport (including bus-service guidance for an approximately 10 km radius), health and wellbeing, technology and administration, student life and careers, and international students and visitors.

## Run on Windows

Open PowerShell in this folder and run:

```powershell
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python app.py
```

Then open <http://127.0.0.1:5000> in your browser. If PowerShell blocks activation, run the app with `\.venv\Scripts\python.exe app.py` instead.

## Run on macOS or Linux

```bash
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

## Customize for your college

Edit `faq_data.py` to add verified Soundarya Institute program lists, official office names, links, phone numbers, library and canteen hours, menus, event calendars, and campus policies. The included answers are general guidance and do not claim to provide current institutional schedules or official policies. Verify institute-specific information before students rely on it. The app is intended as a starting point, not an emergency service; urgent issues should go to campus security or local emergency services.

## Endpoints

- `GET /` — assistant web page
- `POST /api/ask` — accepts JSON such as `{"question":"Where can I get tutoring?"}`
- `GET /api/faqs` — all FAQ entries
- `GET /api/faqs?category=Academics` — FAQs in one category
