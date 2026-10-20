import re
import os

with open('school-report.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the SMC, Affiliation etc. with real certificates if applicable
# Let's just add a section for "Mandatory Certificates" or update existing sections.

# Find the container div end to append a new section for certificates
container_end_idx = content.rfind('</div>\n\n</body>')

certificates = os.listdir('Certificate')
cert_html = '''
        <!-- Certificates -->
        <section id="certificates" class="section">
            <div class="section-title">
                <h2>Official Certificates</h2>
            </div>
            <div class="section-content">
                <div class="card-list">
'''

for cert in certificates:
    if cert.endswith('.pdf'):
        name = cert.replace('.pdf', '').replace('_20250705_0001', '').replace('_20250705_0001 (1)', '')
        cert_html += f'''
                    <div class="card" style="text-align: center;">
                        <h4>{name}</h4>
                        <a href="./Certificate/{cert}" target="_blank" class="btn-download"><i class="fas fa-file-pdf"></i> View Certificate</a>
                    </div>
'''

cert_html += '''
                </div>
            </div>
        </section>
'''

content = content[:container_end_idx] + cert_html + content[container_end_idx:]

with open('school-report.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated school-report.html with certificates.")
