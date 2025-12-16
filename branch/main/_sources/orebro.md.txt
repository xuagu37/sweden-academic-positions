# Örebro University
<p style="font-size: 1.2em; font-weight: bold;">Total positions: 12</p>


<div id="filters" style="margin: 1em 0;">
  <label for="filterType"><strong>Filter by Job Type:</strong></label>
  <select id="filterType" style="margin-right: 1em;">
    <option value="">Show All</option>
    <option value="PhD">PhD</option>
    <option value="Postdoc/Researcher">Postdoc/Researcher</option>
    <option value="Lecturer/Professor">Lecturer/Professor</option>
    <option value="Research Engineer">Research Engineer</option>    
    <option value="Other">Other</option>
  </select>
  <input type="text" id="jobFilter" placeholder="Search jobs..." style="padding: 0.5em; width: 50%;">
</div>

<div id="jobList">
<div class="job" data-type="None" style="margin-bottom: 1.5em;">

</div>

<div class="job" data-type="Other" style="margin-bottom: 1.5em;">
<h3>Laboratory assistant for a study on PFAS in water samples close to a contaminated site</h3>

- **Link:** [View job posting](https://www.oru.se/english/career/available-positions/job/?jid=20250359)
- **Department:** 
- **Published:** 
- **Deadline:** 2025-12-16

</div>

<div class="job" data-type="Postdoc/Researcher" style="margin-bottom: 1.5em;">
<h3>Postdoctoral researcher in Embodied Learning for Underwater Robotics</h3>

- **Link:** [View job posting](https://www.oru.se/english/career/available-positions/job/?jid=20250335)
- **Department:** 
- **Published:** 
- **Deadline:** 2025-12-22

</div>

<div class="job" data-type="Postdoc/Researcher" style="margin-bottom: 1.5em;">
<h3>Postdoctoral researcher in computational metabolomics and exposomics</h3>

- **Link:** [View job posting](https://www.oru.se/english/career/available-positions/job/?jid=20250378)
- **Department:** 
- **Published:** 
- **Deadline:** 2026-01-07

</div>

<div class="job" data-type="PhD" style="margin-bottom: 1.5em;">
<h3>Doctoral student in Computer Science with a focus on large language models in health</h3>

- **Link:** [View job posting](https://www.oru.se/english/career/available-positions/job/?jid=20250373)
- **Department:** 
- **Published:** 
- **Deadline:** 2026-01-09

</div>

<div class="job" data-type="PhD" style="margin-bottom: 1.5em;">
<h3>Doctoral Student in Computer Science with a Focus on Tractable Quantum Machine Learning</h3>

- **Link:** [View job posting](https://www.oru.se/english/career/available-positions/job/?jid=20250374)
- **Department:** 
- **Published:** 
- **Deadline:** 2026-01-12

</div>

<div class="job" data-type="Lecturer/Professor" style="margin-bottom: 1.5em;">
<h3>Professor of Chemistry</h3>

- **Link:** [View job posting](https://www.oru.se/english/career/available-positions/job/?jid=20250354)
- **Department:** 
- **Published:** 
- **Deadline:** 2026-01-12

</div>

<div class="job" data-type="PhD" style="margin-bottom: 1.5em;">
<h3>Doctoral student in Computer Science with a focus on Efficient Methods for Machine Learning</h3>

- **Link:** [View job posting](https://www.oru.se/english/career/available-positions/job/?jid=20250375)
- **Department:** 
- **Published:** 
- **Deadline:** 2026-01-16

</div>

<div class="job" data-type="PhD" style="margin-bottom: 1.5em;">
<h3>Doctoral students in Computer Science with a focus on Neuro-inspired Computing</h3>

- **Link:** [View job posting](https://www.oru.se/english/career/available-positions/job/?jid=20250376)
- **Department:** 
- **Published:** 
- **Deadline:** 2026-01-16

</div>

<div class="job" data-type="Lecturer/Professor" style="margin-bottom: 1.5em;">
<h3>Professor of Business Administration with a specialisation in Organisation</h3>

- **Link:** [View job posting](https://www.oru.se/english/career/available-positions/job/?jid=20250314)
- **Department:** 
- **Published:** 
- **Deadline:** 2026-01-23

</div>

<div class="job" data-type="Lecturer/Professor" style="margin-bottom: 1.5em;">
<h3>Professor of Psychology</h3>

- **Link:** [View job posting](https://www.oru.se/english/career/available-positions/job/?jid=20250339)
- **Department:** 
- **Published:** 
- **Deadline:** 2026-01-31

</div>

<div class="job" data-type="Postdoc/Researcher" style="margin-bottom: 1.5em;">
<h3>Postdoctoral researcher in sociology</h3>

- **Link:** [View job posting](https://www.oru.se/english/career/available-positions/job/?jid=20250333)
- **Department:** 
- **Published:** 
- **Deadline:** 2026-02-02

</div>

<div class="job" data-type="Lecturer/Professor" style="margin-bottom: 1.5em;">
<h3>Professor of Biology specialising in molecular physiology</h3>

- **Link:** [View job posting](https://www.oru.se/english/career/available-positions/job/?jid=20250355)
- **Department:** 
- **Published:** 
- **Deadline:** 2026-02-27
</div></div>

<script>
document.addEventListener("DOMContentLoaded", function () {
  const typeSelect = document.getElementById('filterType');
  const textInput = document.getElementById('jobFilter');
  const jobBlocks = document.querySelectorAll('.job');

  function updateDisplay() {
    const selected = typeSelect.value.toLowerCase();
    const query = textInput.value.toLowerCase();

    jobBlocks.forEach(job => {
      const jobType = (job.dataset.type || "").toLowerCase();
      const matchesType = !selected || jobType === selected;
      const matchesQuery = job.textContent.toLowerCase().includes(query);
      job.style.display = (matchesType && matchesQuery) ? '' : 'none';
    });
  }

  typeSelect.addEventListener('change', updateDisplay);
  textInput.addEventListener('input', updateDisplay);
});
</script>
