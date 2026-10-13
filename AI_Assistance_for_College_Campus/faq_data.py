"""Soundarya Institute campus FAQ starter. Add verified institute-specific details."""

FAQS = [
    # Admissions and enrollment
    {"category": "Admissions", "question": "How do I apply for admission?", "answer": "Apply through the college admissions portal. Review the current program requirements, submit the application and supporting documents, and keep your application reference number. Contact Admissions for program-specific instructions."},
    {"category": "Admissions", "question": "What documents are needed for admission?", "answer": "Requirements vary by program. Common items include academic transcripts, proof of identity, application forms, photographs, and any entrance-test or eligibility records. Confirm the current checklist with Admissions before submitting originals."},
    {"category": "Admissions", "question": "How can I check my application status?", "answer": "Sign in to the admissions portal using the account used to apply. If the status has not changed after the stated processing period, contact Admissions with your application number."},
    {"category": "Admissions", "question": "Can I change my course or major?", "answer": "Usually this requires approval from your academic department and the Registrar, and may depend on prerequisites, seat availability, and deadlines. Ask your advisor before changing enrollment."},
    {"category": "Admissions", "question": "How do I defer admission?", "answer": "Contact Admissions before the enrollment deadline and request the deferral procedure in writing. Deferral eligibility, duration, and deposit treatment depend on college policy."},
    {"category": "Admissions", "question": "Where can I get a student ID?", "answer": "After enrollment, follow the ID-card instructions from Student Services or the Registrar. Bring the requested identity documents and a photo if required."},
    {"category": "Admissions", "question": "How do I register for classes?", "answer": "Use the student portal during your registration window. Check prerequisites, timetable conflicts, credit limits, and any advisor holds before submitting your course selections."},
    {"category": "Admissions", "question": "How do I drop or add a class?", "answer": "Use the registration portal before the published add/drop deadline. Consult your advisor about financial aid, fees, attendance, and transcript effects before dropping a course."},
    {"category": "Admissions", "question": "How do I get an enrollment or bonafide certificate?", "answer": "Request the certificate from the Registrar or Student Services, usually through the student portal. State the purpose and allow time for processing."},
    {"category": "Admissions", "question": "How do I transfer credits?", "answer": "Submit official transcripts and course descriptions to the Registrar or department for evaluation. Credit transfer is subject to equivalency rules and formal approval."},
    # Academics
    {"category": "Academics", "question": "Where can I find my timetable?", "answer": "Check the student portal or your department's official notice board for the latest timetable. Confirm room changes before each class."},
    {"category": "Academics", "question": "Where can I find the academic calendar?", "answer": "The Registrar or Academic Affairs page publishes the official calendar, including term dates, holidays, examination periods, and add/drop deadlines."},
    {"category": "Academics", "question": "How do I contact my professor?", "answer": "Use the email address or office hours listed in the course outline or faculty directory. Include the course code and a clear subject line, and allow a reasonable response time."},
    {"category": "Academics", "question": "What should I do if I miss a class?", "answer": "Check the course learning platform and ask a classmate for notes. Inform your instructor promptly if the absence is documented or affects an assessment; attendance rules vary by course."},
    {"category": "Academics", "question": "How do I report an attendance error?", "answer": "Contact the instructor promptly with the course, date, and any supporting details. If it is not resolved, ask your department office about the review process."},
    {"category": "Academics", "question": "How can I get tutoring?", "answer": "Ask your department or Academic Support Center about peer tutoring, writing support, study groups, and appointment availability."},
    {"category": "Academics", "question": "How do I request an academic transcript?", "answer": "Submit a transcript request through the Registrar's portal or office. Check whether you need an official sealed or electronically verified copy and allow for processing time."},
    {"category": "Academics", "question": "How do I appeal a grade?", "answer": "First discuss the grading feedback with your instructor. If the concern remains, follow the published department or academic appeals procedure before its deadline."},
    {"category": "Academics", "question": "What happens if I fail a course?", "answer": "Options may include repeating the course, taking an approved equivalent, or academic advising. Contact your advisor promptly to understand prerequisites, progression, and financial-aid implications."},
    {"category": "Academics", "question": "Where can I find exam schedules?", "answer": "Exam schedules are posted by the Registrar or department in the student portal. Verify the date, time, room, and permitted materials shortly before the exam."},
    {"category": "Academics", "question": "Can I get an extension on an assignment?", "answer": "Ask your instructor as early as possible, explain the situation, and follow the course policy. Supporting documentation may be required for exceptional circumstances."},
    {"category": "Academics", "question": "How do I withdraw from the college?", "answer": "Speak with your academic advisor and Registrar before submitting the official withdrawal form. Ask about refund dates, housing, financial aid, and access to services."},
    {"category": "Academics", "question": "How do I access the learning management system?", "answer": "Sign in with your campus account through the college portal. If access fails, reset your password or contact the IT Help Desk and include the course name and a screenshot of the error."},
    {"category": "Academics", "question": "How can I get academic accommodations?", "answer": "Contact Disability or Accessibility Services to discuss confidential documentation and accommodations. Begin early because review and coordination can take time."},
    {"category": "Academics", "question": "Where do I report academic integrity concerns?", "answer": "Review the academic integrity policy and contact the instructor or designated Academic Integrity office. Share factual details and preserve relevant records."},
    # Fees and financial aid
    {"category": "Fees & Financial Aid", "question": "How do I pay tuition fees?", "answer": "Use the payment options shown in the student finance portal or contact the Bursar/Finance Office. Verify the account and deadline through official college channels before paying."},
    {"category": "Fees & Financial Aid", "question": "How can I see my fee balance?", "answer": "Sign in to the student finance portal and review your account statement. Contact the Finance Office if a charge or payment is missing."},
    {"category": "Fees & Financial Aid", "question": "Can I pay fees in installments?", "answer": "Ask the Finance Office whether an installment plan is available for your program and term. Confirm enrollment deadlines, plan fees, and due dates in writing."},
    {"category": "Fees & Financial Aid", "question": "How do I apply for a scholarship?", "answer": "Check the official scholarships page for eligibility, required documents, and deadlines. Submit through the stated process and keep confirmation of your application."},
    {"category": "Fees & Financial Aid", "question": "How do I apply for financial aid?", "answer": "Contact the Financial Aid Office and complete the current application forms by their deadlines. Ask what documents are needed and how changes in enrollment affect your aid."},
    {"category": "Fees & Financial Aid", "question": "How do I get a fee receipt?", "answer": "Download the receipt from the student finance portal after payment has posted, or request a copy from the Finance Office."},
    {"category": "Fees & Financial Aid", "question": "How do I request a fee refund?", "answer": "Submit the refund request to the Finance Office with payment details and supporting documents. Refund eligibility and timing depend on the published withdrawal and refund schedule."},
    {"category": "Fees & Financial Aid", "question": "Who can help with an unexpected financial difficulty?", "answer": "Contact Financial Aid or Student Support to ask about emergency grants, payment plans, food assistance, and confidential advice."},
    # Campus services and facilities
    {"category": "Campus Services", "question": "What are the library hours?", "answer": "Check the Library website or entrance notices for current hours, which can change during holidays and exams. The library desk can confirm access to study rooms and services."},
    {"category": "Campus Services", "question": "How do I borrow a library book?", "answer": "Use your student ID at the library desk or self-checkout. Check due dates and renewal limits in your library account."},
    {"category": "Campus Services", "question": "How do I reserve a study room?", "answer": "Use the library's room-booking system or ask the circulation desk. Room size, booking windows, and time limits vary."},
    {"category": "Campus Services", "question": "How do I connect to campus Wi-Fi?", "answer": "Choose the official student network and sign in with your campus credentials. Follow the IT setup guide; never share your password. Contact IT if your device cannot connect."},
    {"category": "Campus Services", "question": "Where can I print or scan documents?", "answer": "Check the library and computer lab facilities for printers, scanners, and current charges. Ask the help desk about setting up print credit."},
    {"category": "Campus Services", "question": "Where can I eat on campus?", "answer": "See the campus dining page or map for cafeterias, vending areas, dietary options, and service hours."},
    {"category": "Campus Services", "question": "How do I find a campus building?", "answer": "Use the campus map on the college website or ask the reception desk. Search by building name or room number and allow time to walk between locations."},
    {"category": "Campus Services", "question": "How can I book a sports facility?", "answer": "Contact Recreation or use the campus booking portal to see facility availability, membership rules, and equipment requirements."},
    {"category": "Campus Services", "question": "Where is the lost and found?", "answer": "Contact Campus Security or Student Services and describe the item, location, and approximate time it was lost. Do not include sensitive personal information in public posts."},
    {"category": "Campus Services", "question": "How do I access a computer lab?", "answer": "Check the department or IT page for lab locations, opening hours, and access rules. Bring your student ID and campus login."},
    {"category": "Campus Services", "question": "Where can I get a locker?", "answer": "Ask Student Services or your department about locker availability, rental terms, and key return requirements."},
    {"category": "Campus Services", "question": "Are campus facilities accessible?", "answer": "Contact Accessibility Services or Facilities for accessible routes, entrances, elevators, and room-specific assistance. Report a blocked accessible route to Campus Facilities promptly."},
    # Housing and transportation
    {"category": "Housing & Transport", "question": "How do I apply for a hostel or residence hall?", "answer": "Apply through Housing/Residence Life using the official application. Check eligibility, deadlines, deposits, meal plans, and room assignment dates."},
    {"category": "Housing & Transport", "question": "How do I report a hostel maintenance issue?", "answer": "Submit a maintenance request through the residence portal or inform the residence office. For an urgent hazard, contact residence staff or Campus Security immediately."},
    {"category": "Housing & Transport", "question": "What should I do if I have a roommate problem?", "answer": "Start with a respectful conversation if safe, then contact your resident advisor or Housing office for mediation and next steps."},
    {"category": "Housing & Transport", "question": "Where can I find campus bus routes?", "answer": "Check the official transport page or campus map for routes, stops, schedules, and service alerts. Confirm holiday schedules before travelling."},
    {"category": "Housing & Transport", "question": "How do I get a parking permit?", "answer": "Apply through Transportation or Campus Security. Review permit zones, fees, waitlists, and visitor parking rules before parking."},
    {"category": "Housing & Transport", "question": "Is bicycle parking available?", "answer": "Use the bicycle racks shown on the campus map and secure your bike with a strong lock. Ask Transportation about registration or sheltered parking."},
    {"category": "Housing & Transport", "question": "How do I report a campus shuttle delay?", "answer": "Check the transport service alerts first, then contact the campus transport desk with the route, stop, and time."},
    {"category": "Housing & Transport", "question": "Does Soundarya Institute provide bus service within a 10 km radius?", "answer": "The campus bus service is intended to support students living within approximately 10 km of the institute. Confirm whether your area and pickup point are covered with the institute transport office, since routes and seat availability may vary."},
    {"category": "Housing & Transport", "question": "How can I check if my area is on a college bus route?", "answer": "Contact the Soundarya Institute transport office with your area or nearest landmark. Ask for the current route map, pickup point, and whether seats are available."},
    {"category": "Housing & Transport", "question": "How do I register for the college bus?", "answer": "Ask the institute transport office how to apply, what documents are needed, and when registration closes. Confirm your approved pickup point before relying on the service."},
    {"category": "Housing & Transport", "question": "What are the college bus timings and pickup points?", "answer": "Bus timings and stops depend on the assigned route and can change. Get the current schedule and pickup details directly from the institute transport office or its official notices."},
    {"category": "Housing & Transport", "question": "How much does the college bus service cost?", "answer": "Bus fees may depend on the route or term. Contact the institute transport office or Finance Office for current charges, payment deadlines, and refund rules."},
    {"category": "Housing & Transport", "question": "What should I do if I miss the college bus?", "answer": "Contact the transport office or the designated route contact for guidance. Do not board another route unless the transport staff confirms it is allowed."},
    {"category": "Housing & Transport", "question": "How do I report a late bus or a change to my pickup point?", "answer": "Notify the institute transport office with your route, stop, and travel time. Request approval before changing your assigned pickup point."},
    # Health, safety and wellbeing
    {"category": "Health & Wellbeing", "question": "Where can I get medical help on campus?", "answer": "Contact the campus health center for routine care and its current hours. For a medical emergency, call your local emergency number or Campus Security immediately."},
    {"category": "Health & Wellbeing", "question": "How do I book a counselling appointment?", "answer": "Contact Counselling or Student Wellbeing Services through their official phone, email, or booking portal. Ask about confidentiality, urgent support, and available appointment formats."},
    {"category": "Health & Wellbeing", "question": "What should I do in an emergency?", "answer": "Call the local emergency number or Campus Security. Give the exact building, floor, and room, follow dispatcher instructions, and do not put yourself in danger."},
    {"category": "Health & Wellbeing", "question": "How do I report harassment or discrimination?", "answer": "Contact the designated Equity, Title IX/equivalent, Student Conduct, or safeguarding office using the college's official reporting process. If anyone is in immediate danger, contact emergency services."},
    {"category": "Health & Wellbeing", "question": "How do I report a safety hazard?", "answer": "Notify Campus Security or Facilities with the location and nature of the hazard. For immediate danger, call emergency services and keep others at a safe distance if possible."},
    {"category": "Health & Wellbeing", "question": "Is there support for stress or mental health?", "answer": "Student Wellbeing or Counselling can discuss confidential support and referrals. If there is an immediate risk of harm, contact emergency services or a crisis service in your area now."},
    {"category": "Health & Wellbeing", "question": "How do I request disability support?", "answer": "Contact Accessibility Services to start a confidential conversation about accommodations, assistive technology, and documentation."},
    {"category": "Health & Wellbeing", "question": "Where do I report a fire or suspicious activity?", "answer": "Call emergency services or Campus Security immediately and follow posted evacuation instructions. Do not investigate or confront anyone yourself."},
    # Technology and administration
    {"category": "Technology & Admin", "question": "I forgot my campus password. What should I do?", "answer": "Use the official password-reset page. If recovery fails, contact the IT Help Desk and be ready to verify your identity. Never send your password by email."},
    {"category": "Technology & Admin", "question": "How do I get help from IT?", "answer": "Submit a ticket through the campus IT portal or contact the Help Desk. Include your device, service, error message, and the best way to reach you; exclude passwords."},
    {"category": "Technology & Admin", "question": "How do I get a student email account?", "answer": "Your campus email is usually activated after enrollment. Sign in through the official portal with your campus credentials or contact IT if the account is missing."},
    {"category": "Technology & Admin", "question": "How do I update my personal details?", "answer": "Use the student portal or contact the Registrar. Some changes, such as legal name or residency, may require supporting documents."},
    {"category": "Technology & Admin", "question": "How do I replace a lost student ID?", "answer": "Report the loss to Student Services or Campus Security, then request a replacement through the ID office. Ask whether the old card must be deactivated and whether a fee applies."},
    {"category": "Technology & Admin", "question": "How do I submit a general complaint or suggestion?", "answer": "Use the college's official feedback or complaint channel. Include relevant dates and facts, and keep a copy of your submission."},
    {"category": "Technology & Admin", "question": "How do I get an official letter for a visa or internship?", "answer": "Request it from the Registrar or International Student Office, explaining the purpose and required details. Processing time and supporting documents may vary."},
    {"category": "Technology & Admin", "question": "How do I protect my account from phishing?", "answer": "Do not open unexpected links or share passwords or verification codes. Report suspicious messages to IT using the official reporting method."},
    # Student life and careers
    {"category": "Student Life & Careers", "question": "How do I join a student club?", "answer": "Browse the Student Affairs clubs directory or attend the student activities fair. Contact the club for meeting times, membership requirements, and accessibility details."},
    {"category": "Student Life & Careers", "question": "How do I start a new student club?", "answer": "Ask Student Affairs for recognition requirements, advisor rules, constitution templates, and funding deadlines. Submit the required application before advertising as an official club."},
    {"category": "Student Life & Careers", "question": "Where can I find campus events?", "answer": "Check the official events calendar, Student Affairs channels, and department announcements. Confirm registration and venue details with the event organizer."},
    {"category": "Student Life & Careers", "question": "How do I find an internship or job?", "answer": "Contact Career Services for job boards, resume reviews, interview practice, and internship guidance. Verify position details with the employer and follow college placement rules."},
    {"category": "Student Life & Careers", "question": "How do I book a career advising appointment?", "answer": "Use the Career Services booking portal or contact their office. Bring your resume and questions about your goals or applications."},
    {"category": "Student Life & Careers", "question": "Where can I volunteer?", "answer": "Check the Student Affairs or community engagement office for approved opportunities, schedules, and any required training."},
    {"category": "Student Life & Careers", "question": "How do I get a campus job?", "answer": "Look at the college's student employment portal and ask Career Services about eligibility, work-study rules, and application support."},
    {"category": "Student Life & Careers", "question": "How do I request a graduation certificate?", "answer": "Confirm graduation eligibility with your department and Registrar, apply by the stated deadline, and check separately for ceremony registration and certificate delivery."},
    {"category": "Student Life & Careers", "question": "How can I get food assistance?", "answer": "Contact Student Support, Student Affairs, or the campus food pantry. They can explain confidential eligibility and available resources."},
    # Library
    {"category": "Library", "question": "Where is the library at Soundarya Institute?", "answer": "Please check the institute campus map or ask the reception/student office for the current library location and directions."},
    {"category": "Library", "question": "What are the library timings?", "answer": "Library hours can change during exams, holidays, and breaks. Check the latest notice from Soundarya Institute or confirm with the library desk before visiting."},
    {"category": "Library", "question": "What can I do in the library?", "answer": "Ask the Soundarya Institute library about available books, reference materials, reading areas, digital resources, and any student facilities. Current services should be confirmed with the library."},
    {"category": "Library", "question": "How do I borrow or return a library book?", "answer": "Bring your student ID and ask the library desk about borrowing, return dates, renewals, and late-return rules. The library can confirm the current process."},
    {"category": "Library", "question": "Can I renew a library book?", "answer": "Renewal eligibility and limits depend on the library's rules and whether another student has requested the book. Contact the library desk before the due date."},
    {"category": "Library", "question": "How do I find a book or reference material?", "answer": "Ask library staff for help searching the catalogue or locating material by subject, title, or author. Share your course or topic to get more useful guidance."},
    {"category": "Library", "question": "Can I study quietly in the library?", "answer": "Ask library staff about quiet study areas, group-study rules, and current seating availability. Please follow posted noise and phone-use guidelines."},
    {"category": "Library", "question": "Can I use library resources for assignments?", "answer": "The library can help you locate relevant books and other available resources. Ask staff or your faculty for guidance on credible sources and citation requirements."},
    {"category": "Library", "question": "What should I do if I lose a library book?", "answer": "Contact the library desk as soon as possible. Staff can explain the replacement, fine, or lost-item procedure that applies."},
    # Canteen
    {"category": "Canteen", "question": "Where is the canteen at Soundarya Institute?", "answer": "Please check the campus map or ask reception or Student Services for directions to the canteen."},
    {"category": "Canteen", "question": "What are the canteen timings?", "answer": "Canteen hours may vary by class schedule, holidays, and college events. Check current campus notices or confirm with canteen staff."},
    {"category": "Canteen", "question": "What food is available in the canteen?", "answer": "A starter sample menu of common South Indian dishes: idli (2 pieces) ₹30, medu vada ₹25, upma ₹40, pongal ₹50, plain dosa ₹50, masala dosa ₹70, lemon rice ₹50, curd rice ₹50, vegetable meals ₹90, and filter coffee ₹20. These are example prices for this project, not confirmed Soundarya Institute prices. Please check the canteen notice board or ask staff for today's menu and actual rates."},
    {"category": "Canteen", "question": "What are some South Indian dishes and their prices?", "answer": "Sample canteen menu prices in rupees: idli (2 pieces) ₹30; medu vada ₹25; upma ₹40; pongal ₹50; plain dosa ₹50; masala dosa ₹70; lemon rice ₹50; curd rice ₹50; vegetable meals ₹90; filter coffee ₹20. These are illustrative starter prices, not verified Soundarya Institute rates. Please confirm today's menu and prices with canteen staff."},
    {"category": "Canteen", "question": "Does the canteen have vegetarian food?", "answer": "Ask canteen staff which vegetarian options are available that day and how they are prepared."},
    {"category": "Canteen", "question": "Can I ask about food allergies or ingredients?", "answer": "Speak directly with canteen staff before ordering and explain the allergy. They can confirm available ingredient information; avoid any item if its safety is uncertain."},
    {"category": "Canteen", "question": "How can I share feedback about the canteen?", "answer": "Share your feedback with canteen management or the college office responsible for student services. Include the date and details so the concern can be reviewed."},
    # Programs and courses
    {"category": "Programs", "question": "What programs are offered at Soundarya Institute of Management and Science?", "answer": "Program offerings and eligibility can change. Please consult the current Soundarya Institute admissions prospectus or contact Admissions for the verified list of programs, specializations, and intake details."},
    {"category": "Programs", "question": "How do I choose a program?", "answer": "Compare the current program curriculum, eligibility, duration, learning outcomes, and career pathways in the institute prospectus. You can also ask Admissions or the relevant department for academic guidance."},
    {"category": "Programs", "question": "What are the eligibility requirements for a program?", "answer": "Eligibility depends on the program and admission year. Check the latest official prospectus or confirm the requirements with Soundarya Institute Admissions before applying."},
    {"category": "Programs", "question": "Where can I find the course syllabus?", "answer": "Ask your department or faculty for the current syllabus and course plan. The department can confirm which version applies to your program and admission year."},
    {"category": "Programs", "question": "Can I change my program or specialization?", "answer": "Program changes depend on institute rules, eligibility, available seats, and deadlines. Speak with your department and Admissions before making a decision."},
    {"category": "Programs", "question": "Who can explain career options after my program?", "answer": "Ask your department faculty or the institute's placement/career support office about career paths, internships, and further-study options related to your program."},
    # Events
    {"category": "Events", "question": "What events are happening at Soundarya Institute?", "answer": "Check the latest institute announcements, department notices, and official event channels for upcoming programs, workshops, cultural activities, and academic events."},
    {"category": "Events", "question": "How do I register for a college event?", "answer": "Follow the registration instructions in the event announcement. Check whether registration is required, who may attend, and the deadline."},
    {"category": "Events", "question": "Where and when is an event taking place?", "answer": "Refer to the event's latest official notice for its date, time, venue, and any changes. If details are missing, contact the event organizer or department."},
    {"category": "Events", "question": "How can I participate in cultural or sports events?", "answer": "Watch institute and department announcements for auditions, team selections, sign-ups, and practice schedules. Contact the organizer for eligibility and participation details."},
    {"category": "Events", "question": "How can I organize a student event?", "answer": "Ask Student Affairs or your department about event approval, faculty sponsorship, venue booking, budget, safety, and publicity requirements before making commitments."},
    {"category": "Events", "question": "How do I get a certificate for attending an event?", "answer": "Ask the event organizer whether attendance certificates are issued and how they are distributed. Keep your registration or attendance confirmation if provided."},
    # International and visitors
    {"category": "International & Visitors", "question": "Where can international students get help?", "answer": "Contact the International Student Office for immigration guidance, orientation, travel signatures, and cultural support. For immigration decisions, follow official government guidance and qualified advice."},
    {"category": "International & Visitors", "question": "How do I find campus orientation information?", "answer": "Check the Admissions or Student Affairs orientation page for dates, registration, checklists, and new-student sessions."},
    {"category": "International & Visitors", "question": "Where can visitors park or check in?", "answer": "Review the campus visitor page for parking, building access, and check-in rules. Visitors may need to register with reception or Campus Security."},
    {"category": "International & Visitors", "question": "How do I invite a guest to campus?", "answer": "Follow the event or department visitor procedure. The host should confirm access requirements, guest parking, and any identification needed."},
    {"category": "International & Visitors", "question": "Who can help with language support?", "answer": "Ask the International Student Office, Writing Center, or Student Support about language classes, conversation groups, and interpreting services."},
]

FALLBACK = "I couldn't find a close answer in the campus guide. Try a different wording or contact the relevant college office. For urgent safety or medical help, contact emergency services or Campus Security now."


def get_categories():
    return list(dict.fromkeys(item["category"] for item in FAQS))


def _tokens(text):
    import re

    return set(re.findall(r"[a-z0-9]+", text.lower()))


def find_answers(question, limit=3):
    """Return simple keyword-ranked FAQ matches without external AI services."""
    query = _tokens(question)
    if not query:
        return [{"category": "General", "question": "", "answer": FALLBACK}]
    scored = []
    for item in FAQS:
        q_tokens = _tokens(item["question"])
        a_tokens = _tokens(item["answer"])
        overlap = query & q_tokens
        score = len(overlap) * 3 + len(query & a_tokens) * 0.35
        if item["question"].lower().rstrip("?") in question.lower():
            score += 5
        if score:
            scored.append((score, item))
    scored.sort(key=lambda result: result[0], reverse=True)
    if not scored or scored[0][0] < 1.5:
        return [{"category": "General", "question": "", "answer": FALLBACK}]
    return [item for _, item in scored[:limit]]
