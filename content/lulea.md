# Luleå University
<p style="font-size: 1.2em; font-weight: bold;">Total positions: 10</p>


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

<div class="job" data-type="PhD" style="margin-bottom: 1.5em;">
<h3>PhD Student in Signal Processing</h3>

- **Link:** [View job posting](https://www.ltu.se/en/about-ltu/work-at-ltu/vacant-positions#item-8973)
- **Department:** 
- **Published:** 
- **Deadline:** 2025-05-11

</div>

<div class="job" data-type="PhD" style="margin-bottom: 1.5em;">
<h3>PhD student in Electronic Systems with focus on electrodynamic modeling</h3>

- **Link:** [View job posting](https://www.ltu.se/en/about-ltu/work-at-ltu/vacant-positions#item-9055)
- **Department:** 
- **Published:** 
- **Deadline:** 2025-05-15

</div>

<div class="job" data-type="PhD" style="margin-bottom: 1.5em;">
<h3>PhD Student position in Machine Learning focus Sustainable Machine Learning</h3>

- **Link:** [View job posting](https://www.ltu.se/en/about-ltu/work-at-ltu/vacant-positions#item-9028)
- **Department:** 
- **Published:** 
- **Deadline:** 2025-05-15

</div>

<div class="job" data-type="Research Engineer" style="margin-bottom: 1.5em;">
<h3>Research Engineers, summer internship, Robotics and Artificial Intelligence</h3>

- **Link:** [View job posting](https://www.ltu.se/en/about-ltu/work-at-ltu/vacant-positions#item-9013)
- **Department:** 
- **Published:** 
- **Deadline:** 2025-05-20

</div>

<div class="job" data-type="Lecturer/Professor" style="margin-bottom: 1.5em;">
<h3>Associated Senior Lecturer in Robotics and AI</h3>

- **Link:** [View job posting](https://www.ltu.se/en/about-ltu/work-at-ltu/vacant-positions#item-9093)
- **Department:** 
- **Published:** 
- **Deadline:** 2025-05-23

</div>

<div class="job" data-type="Other" style="margin-bottom: 1.5em;">
<h3>Summer student in Cyber-Physical Systems</h3>

- **Link:** [View job posting](https://www.ltu.se/en/about-ltu/work-at-ltu/vacant-positions#item-9073)
- **Department:** 
- **Published:** 
- **Deadline:** 2025-05-25

</div>

<div class="job" data-type="PhD" style="margin-bottom: 1.5em;">
<h3>PhD Student in Engineering Materials with specialization in steel recycling and anti-alloying</h3>

- **Link:** [View job posting](https://www.ltu.se/en/about-ltu/work-at-ltu/vacant-positions#item-9079)
- **Department:** 
- **Published:** 
- **Deadline:** 2025-05-26

</div>

<div class="job" data-type="PhD" style="margin-bottom: 1.5em;">
<h3>PhD Position in Engineering Materials – Advanced Microstructural Characteriza-tion of Ausferritic Steels</h3>

- **Link:** [View job posting](https://www.ltu.se/en/about-ltu/work-at-ltu/vacant-positions#item-9090)
- **Department:** 
- **Published:** 
- **Deadline:** 2025-05-28

</div>

<div class="job" data-type="Lecturer/Professor" style="margin-bottom: 1.5em;">
<h3>​​Professor/Head of Subject of Cyber-Physical Systems​</h3>

- **Link:** [View job posting](https://www.ltu.se/en/about-ltu/work-at-ltu/vacant-positions#item-8922)
- **Department:** 
- **Published:** 
- **Deadline:** 2025-05-31

</div>

<div class="job" data-type="PhD" style="margin-bottom: 1.5em;">
<h3>PhD Student in Cyber-physical systems</h3>

- **Link:** [View job posting](https://www.ltu.se/en/about-ltu/work-at-ltu/vacant-positions#item-9076)
- **Department:** 
- **Published:** 
- **Deadline:** 2025-06-15
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
