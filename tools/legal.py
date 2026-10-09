"""Generate the legal pages for laurenrubalmd.com from site/index.html's header and footer.
Usage: python3 tools/legal.py site <BUILD>   (then: python3 tools/seo.py site)"""
import sys, os, re
SITE, BUILD = sys.argv[1], sys.argv[2]
NAME = "Lauren Rubal, MD"
ENTITY = 'Lauren Rubal, MD <span class="todo">[CONFIRM legal entity name]</span>'
EMAIL = '<span class="todo">[CONFIRM office email]</span>'
PHONE = '<a href="tel:+19494156704">(949) 415-6704</a>'
ADDR = "31551 Camino Capistrano, Suite D<br>San Juan Capistrano, CA 92675"
UPDATED = "October 2026"
CONTACT = f'<div class="box">{ENTITY}<br>{ADDR}<br>Phone: {PHONE}<br>Fax: (949) 269-3263<br>Email: {EMAIL}</div>'

def ul(*items): return "<ul>" + "".join(f"<li>{i}</li>" for i in items) + "</ul>"

PAGES = {
"privacy-policy": dict(eyebrow="Legal", title="Privacy Policy",
 lede="How information is collected, used and protected when you visit this website.", date=f"Last updated: {UPDATED}",
 intro=f"{NAME} respects your privacy. This website Privacy Policy is separate from our <a href=\"notice-of-privacy-practices.html\">Notice of Privacy Practices</a>, which describes how we may use and disclose protected health information in connection with your medical care.",
 sections=[
 ("Information you provide to us", "<p>We may collect information you choose to provide through this website, such as your name, email address, telephone number, appointment request details, or other information you submit.</p><p>At this time, the forms on this website do not send information to us. To request an appointment, please call " + PHONE + ".</p><p>Please do not use general website forms or ordinary email to send sensitive medical information. Patients should use the secure communication method provided by the practice for medical information.</p>"),
 ("Information collected automatically", "<p>When you visit this website, our hosting provider automatically receives technical information needed to deliver and protect the site, such as your IP address, browser type, device type, the pages you request and the referring website.</p><p>We do not currently use analytics services, advertising pixels or similar tracking technologies on this website. If that changes, we will update this Privacy Policy.</p>"),
 ("How we use information", "<p>We may use information collected through this website to:</p>" + ul("Respond to appointment requests and inquiries","Communicate with you","Operate, secure and improve the website","Comply with legal obligations") + "<p>We do not sell personal information collected through this website.</p>"),
 ("Health information", "<p>Information we receive or maintain in connection with providing healthcare may be protected by federal and California health privacy laws. Our use and disclosure of protected health information is governed by our <a href=\"notice-of-privacy-practices.html\">Notice of Privacy Practices</a>, not solely by this website Privacy Policy.</p>"),
 ("Third-party services", "<p>We use third-party companies to help operate this website. They may process information under their own privacy practices and, where required, contractual privacy and security obligations. Currently, they include:</p>" + ul("<strong>Website hosting.</strong> Cloudflare hosts and delivers this website and receives the technical information described above.","<strong>Fonts.</strong> The fonts on this website are served from our own site. Your browser does not contact a third-party font service.","<strong>Maps.</strong> Our contact page displays an embedded Google Map. When it loads, Google receives your IP address and browser information and may set its own cookies.","<strong>Links.</strong> Links to outside websites, such as map directions or social media, share information with those services only if you click them.")),
 ("Cookies and similar technologies", "<p>This website does not set its own cookies or use browser storage to identify or track visitors. The embedded Google Map on our contact page may set its own cookies under Google\u2019s policies. You can control cookies through your browser settings.</p>"),
 ("Security", "<p>We use reasonable administrative, technical and physical safeguards designed to protect information. No website, email system or electronic transmission can be guaranteed to be completely secure.</p>"),
 ("Links to other websites", f"<p>This website may contain links to third-party websites. {NAME} is not responsible for the privacy practices or content of those websites.</p>"),
 ("Children", "<p>This website is not directed to children for independent use. Parents or legal guardians should contact the practice regarding care for a minor.</p>"),
 ("Changes to this policy", "<p>We may update this Privacy Policy as our website, services or legal obligations change. The current version will be posted here with its revision date.</p>"),
 ("Contact us", "<p>Questions about this Privacy Policy may be directed to:</p>" + CONTACT),
 ]),

"notice-of-privacy-practices": dict(eyebrow="Legal", title="Notice of Privacy Practices",
 lede="Your information. Your rights. Our responsibilities.", date="Effective date: <span class=\"todo\">[CONFIRM effective date]</span>",
 intro=f"<strong>This notice describes how medical information about you may be used and disclosed and how you can get access to this information. Please review it carefully.</strong></p><p>{NAME} is committed to protecting the privacy and security of your health information.",
 sections=[
 ("Your rights", "<p>When it comes to your health information, you have certain rights. This section explains your rights and some of our responsibilities to help you.</p>"
  "<h3>Get an electronic or paper copy of your medical record</h3><p>You can ask to see or get an electronic or paper copy of your medical record and other health information we have about you. Ask us how to do this. We will provide a copy or a summary of your health information within the time required by law. We may charge a reasonable, cost-based fee.</p>"
  "<h3>Ask us to correct your medical record</h3><p>You can ask us to correct health information about you that you think is incorrect or incomplete. Ask us how to do this. We may say “no” to your request, but we will tell you why in writing within 60 days.</p>"
  "<h3>Request confidential communications</h3><p>You can ask us to contact you in a specific way (for example, home or office phone) or to send mail to a different address. We will say “yes” to all reasonable requests.</p>"
  "<h3>Ask us to limit what we use or share</h3><p>You can ask us not to use or share certain health information for treatment, payment or our operations. We are not required to agree to your request, and we may say “no” if it would affect your care.</p><p>If you pay for a service or health care item out of pocket in full, you can ask us not to share that information for the purpose of payment or our operations with your health insurer. We will say “yes” unless a law requires us to share that information.</p>"
  "<h3>Get a list of those with whom we’ve shared information</h3><p>You can ask for a list (accounting) of the times we’ve shared your health information for six years prior to the date you ask, who we shared it with and why. We will include all the disclosures except for those about treatment, payment and health care operations, and certain other disclosures (such as any you asked us to make). We’ll provide one accounting a year for free but will charge a reasonable, cost-based fee if you ask for another one within 12 months.</p>"
  "<h3>Get a copy of this privacy notice</h3><p>You can ask for a paper copy of this notice at any time, even if you have agreed to receive the notice electronically. We will provide you with a paper copy promptly.</p>"
  "<h3>Choose someone to act for you</h3><p>If you have given someone medical power of attorney or if someone is your legal guardian, that person can exercise your rights and make choices about your health information. We will make sure the person has this authority and can act for you before we take any action.</p>"
  "<h3>File a complaint if you feel your rights are violated</h3><p>You can complain if you feel we have violated your rights by contacting us using the information at the end of this notice.</p><p>You can also file a complaint with the U.S. Department of Health and Human Services Office for Civil Rights by sending a letter to 200 Independence Avenue, S.W., Washington, D.C. 20201, calling 1-877-696-6775, or visiting <a href=\"https://www.hhs.gov/hipaa/filing-a-complaint/\" target=\"_blank\" rel=\"noopener\">hhs.gov/hipaa/filing-a-complaint</a>.</p><p>We will not retaliate against you for filing a complaint.</p>"),
 ("Your choices", "<p>For certain health information, you can tell us your choices about what we share. If you have a clear preference for how we share your information in the situations described below, talk to us. Tell us what you want us to do, and we will follow your instructions.</p><p>In these cases, you have both the right and choice to tell us to:</p>" + ul("Share information with your family, close friends or others involved in your care","Share information in a disaster relief situation") + "<p>If you are not able to tell us your preference, for example if you are unconscious, we may go ahead and share your information if we believe it is in your best interest. We may also share your information when needed to lessen a serious and imminent threat to health or safety.</p><p>In these cases, we never share your information unless you give us written permission:</p>" + ul("Marketing purposes","Sale of your information","Most sharing of psychotherapy notes")),
 ("Our uses and disclosures", "<p>We typically use or share your health information in the following ways.</p>"
  "<h3>Treat you</h3><p>We can use your health information and share it with other professionals who are treating you. For example, Dr. Rubal may share information with your primary care physician, a laboratory or a pharmacy involved in your care.</p>"
  "<h3>Run our practice</h3><p>We can use and share your health information to run our practice, improve your care and contact you when necessary. For example, we may use your health information to manage your appointments and review the quality of our care.</p>"
  "<h3>Bill for your services</h3><p>We can use and share your health information to bill and get payment from health plans or other entities, or to provide you with documentation you request for your own reimbursement. <span class=\"todo\">[CONFIRM whether the practice bills insurance or is self-pay, and reword to match]</span></p>"),
 ("Other ways we may use or share your information", "<p>We are allowed or required to share your information in other ways, usually in ways that contribute to the public good, such as public health and research. We have to meet many conditions in the law before we can share your information for these purposes.</p>"
  "<h3>Help with public health and safety issues</h3>" + ul("Preventing disease","Helping with product recalls","Reporting adverse reactions to medications","Reporting suspected abuse, neglect or domestic violence","Preventing or reducing a serious threat to anyone’s health or safety") +
  "<h3>Do research</h3><p>We can use or share your information for health research.</p>"
  "<h3>Comply with the law</h3><p>We will share information about you if state or federal laws require it, including with the Department of Health and Human Services if it wants to see that we are complying with federal privacy law.</p>"
  "<h3>Respond to organ and tissue donation requests</h3><p>We can share health information about you with organ procurement organizations.</p>"
  "<h3>Work with a medical examiner or funeral director</h3><p>We can share health information with a coroner, medical examiner or funeral director when an individual dies.</p>"
  "<h3>Address workers’ compensation, law enforcement and other government requests</h3>" + ul("For workers’ compensation claims","For law enforcement purposes or with a law enforcement official, as permitted by law","With health oversight agencies for activities authorized by law","For special government functions such as military, national security and presidential protective services") +
  "<h3>Respond to lawsuits and legal actions</h3><p>We can share health information about you in response to a court or administrative order, or in response to a subpoena.</p>"
  "<h3>More protective laws</h3><p>California law and other laws may give certain health information, including reproductive health information, more protection than federal law. When a more protective law applies, we follow it.</p>"),
 ("Substance use disorder treatment records", "<p>Some substance use disorder treatment records are protected by federal confidentiality rules (42 CFR Part 2). If we receive or maintain records that are subject to these rules, we will use and disclose them only as those rules permit.</p><p>These records, and testimony relaying their content, will not be used or disclosed in any civil, criminal, administrative or legislative proceeding against you unless you give written consent, or a court issues an order after you, or the holder of the records, receive notice and an opportunity to be heard. A court order authorizing use or disclosure must be accompanied by a subpoena or other legal requirement compelling disclosure.</p>"),
 ("Information shared with others", "<p>When we share your health information as this notice permits, the person or organization that receives it may share it again, and it may no longer be protected by the federal privacy rules.</p>"),
 ("Our responsibilities", ul("We are required by law to maintain the privacy and security of your protected health information.","We will let you know promptly if a breach occurs that may have compromised the privacy or security of your information.","We must follow the duties and privacy practices described in this notice and give you a copy of it.","We will not use or share your information other than as described here unless you tell us we can in writing. If you tell us we can, you may change your mind at any time. Let us know in writing if you change your mind.")),
 ("Changes to this notice", "<p>We can change the terms of this notice, and the changes will apply to all information we have about you. The new notice will be available upon request, in our office and on our website.</p>"),
 ("Questions or complaints", CONTACT + "<p style=\"margin-top:14px\">Privacy Officer: <span class=\"todo\">[CONFIRM Privacy Officer name]</span></p><p>You may also file a complaint with the U.S. Department of Health and Human Services Office for Civil Rights at <a href=\"https://www.hhs.gov/hipaa/filing-a-complaint/\" target=\"_blank\" rel=\"noopener\">hhs.gov/hipaa/filing-a-complaint</a>. We will not retaliate against you for filing a complaint.</p>"),
 ]),

"good-faith-estimate": dict(eyebrow="Legal", title="Your Right to a Good Faith Estimate",
 lede="Know what your care is expected to cost.", date=f"Last updated: {UPDATED}",
 intro="Under federal law, healthcare providers must generally give patients who do not have insurance, or who are not using insurance to pay for their care, an estimate of the expected cost of scheduled healthcare services. This is called a Good Faith Estimate.",
 sections=[
 ("You have the right to receive a Good Faith Estimate", "<p>If you do not have health insurance or do not plan to use insurance to pay for your care, you may request a written Good Faith Estimate of expected charges.</p><p>When care is scheduled sufficiently in advance, federal law may also require us to provide an estimate without you requesting one. Your estimate will include the expected charges for items or services reasonably expected to be provided as part of your scheduled care. It is based on information known when it is prepared, and your actual care needs may change.</p>"),
 ("When will I receive it?", ul("If you schedule care at least 3 business days in advance, you should receive a Good Faith Estimate in writing within 1 business day after scheduling.","If you schedule care at least 10 business days in advance, you should receive it within 3 business days after scheduling.","If you ask for a Good Faith Estimate before scheduling care, you should receive it within 3 business days after your request.") + "<p>Please keep a copy or picture of your Good Faith Estimate.</p>"),
 ("What if my bill is higher than the estimate?", "<p>If you receive a bill that is at least $400 more than your Good Faith Estimate from any provider or facility, you can dispute the bill through the federal patient-provider dispute resolution process.</p><p>You must start the dispute within 120 calendar days (about 4 months) of the date on the original bill. There is a $25 administrative fee to use the dispute process.</p><p>To learn more or start a dispute, visit <a href=\"https://www.cms.gov/medical-bill-rights\" target=\"_blank\" rel=\"noopener\">cms.gov/medical-bill-rights</a>, email FederalPPDRQuestions@cms.hhs.gov or call 1-800-985-3059.</p>"),
 ("Questions about your estimate?", CONTACT + "<p style=\"margin-top:14px\">This notice does not itself constitute a Good Faith Estimate.</p>"),
 ]),

"terms-of-use": dict(eyebrow="Legal", title="Terms of Use",
 lede="The terms that apply when you use this website.", date=f"Last updated: {UPDATED}",
 intro=f"These Terms of Use apply to your use of the {NAME} website. By using this website, you agree to these Terms.",
 sections=[
 ("Not medical advice", "<p>The information on this website is provided for general educational and informational purposes only. It is not intended to diagnose or treat any medical condition and is not a substitute for advice from a qualified healthcare professional who knows your individual medical history.</p><p>Do not disregard professional medical advice or delay seeking care because of information you have read on this website.</p>"),
 ("No physician-patient relationship", f"<p>Using this website, reading its content or submitting a general inquiry does not by itself establish a physician-patient relationship with Dr. Lauren Rubal. A physician-patient relationship is established only through the practice’s patient intake and care process.</p>"),
 ("Emergencies", "<p>Do not use this website to seek emergency medical care. If you believe you are experiencing a medical emergency, call 911 or seek immediate emergency medical attention.</p>"),
 ("Appointment requests", "<p>Submitting an appointment request does not guarantee an appointment. An appointment is confirmed only after the practice contacts you and completes its confirmation process.</p>"),
 ("Accuracy of information", "<p>We make reasonable efforts to provide useful and accurate information, but medical knowledge, practice policies and other information may change. We may update website content without notice.</p>"),
 ("Third-party websites", "<p>This website may link to websites or services operated by third parties. We do not control those services and are not responsible for their content, availability, security or privacy practices.</p>"),
 ("Intellectual property", f"<p>Unless otherwise indicated, the text, graphics, branding, photographs and other original content on this website are owned by or licensed to {NAME} and are protected by applicable intellectual property laws. You may view and use the website for personal, noncommercial purposes.</p>"),
 ("Website availability", "<p>We do not guarantee that the website will always be available, uninterrupted or free from errors. We may modify, suspend or discontinue portions of the website when necessary.</p>"),
 ("Privacy", "<p>Your use of this website is also subject to our <a href=\"privacy-policy.html\">Privacy Policy</a>. Health information maintained in connection with healthcare services is addressed in our <a href=\"notice-of-privacy-practices.html\">Notice of Privacy Practices</a>.</p>"),
 ("Changes to these Terms", "<p>We may update these Terms of Use from time to time. The current version and revision date will be posted on this page.</p>"),
 ("Contact", CONTACT),
 ]),

"accessibility": dict(eyebrow="Accessibility", title="Accessibility Statement",
 lede="We want this website to work for everyone.", date=f"Last updated: {UPDATED}",
 intro=f"{NAME} is committed to providing a website that is accessible and usable for all visitors, including people with disabilities. We continue to work to improve the accessibility, usability and clarity of this website.",
 sections=[
 ("Need help accessing something?", "<p>If you have difficulty accessing any part of this website, encounter an accessibility barrier or need information in another format, please contact us. We will make reasonable efforts to provide the information or assistance you need through an accessible method.</p>" + CONTACT + "<p style=\"margin-top:14px\">When contacting us, it helps to tell us which page or feature caused difficulty and the type of assistance you need.</p>"),
 ("Language assistance", "<p>Dr. Rubal speaks English and Spanish. Se habla español.</p>"),
 ("Ongoing accessibility", "<p>Accessibility is an ongoing effort. As the website changes, we will continue to review its accessibility and make improvements where appropriate.</p>"),
 ]),
}

idx = open(os.path.join(SITE, "index.html")).read()
pre = idx.split('<title>')[0]
post_head = idx.split('<link rel="icon"')[1].split('<script type="application/ld+json">')[0]
body_open = idx.split('</head>')[1].split('<section class="hero">')[0]
footer = '<footer class="site">' + idx.split('<footer class="site">')[1]

def slug(t): return re.sub(r'[^a-z0-9]+', '-', t.lower()).strip('-')

for key, p in PAGES.items():
    toc = "".join(f'<li><a href="#{slug(h)}">{h}</a></li>' for h, _ in p["sections"])
    secs = "".join(f'<h2 id="{slug(h)}">{h}</h2>{b}' for h, b in p["sections"])
    desc = re.sub("<[^>]+>", "", p["lede"])
    html = (pre + f'<title>{p["title"]} | {NAME}</title>\n<meta name="description" content="{desc}">\n<meta name="theme-color" content="#F9F6F2">\n<link rel="icon"' + post_head + '</head>' + body_open +
      f'''<section class="legal-head"><div class="wrap"><span class="eyebrow">{p["eyebrow"]}</span><h1>{p["title"]}</h1><p>{p["lede"]}</p><p class="date">{p["date"]}</p></div></section>
<div class="wrap legal">
<aside><span class="eyebrow">On this page</span><ol>{toc}</ol><div class="ask"><span class="eyebrow">Questions?</span>{PHONE}</div></aside>
<article><p class="intro">{p["intro"]}</p>{secs}</article>
</div>
''' + footer)
    html = re.sub(r'Build \d+', f'Build {BUILD}', html)
    open(os.path.join(SITE, key + ".html"), "w").write(html)
    print("wrote", key)
