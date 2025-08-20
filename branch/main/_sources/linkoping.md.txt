# Linköping University
<p style="font-size: 1.2em; font-weight: bold;">Total positions: 16</p>


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

<div class="job" data-type="Lecturer/Professor" style="margin-bottom: 1.5em;">
<h3>WISE Fellow: Assistant professor in Materials Science with focus on Materials for Quantum Technologies</h3>

- **Link:** [View job posting](https://liu.se/en/work-at-liu/vacancies/27157)
- **Department:** 
- **Published:** 
- **Deadline:** 2025-10-06

</div>

<div class="job" data-type="Lecturer/Professor" style="margin-bottom: 1.5em;">
<h3>Professor in Environmental Change</h3>

- **Link:** [View job posting](https://liu.se/en/work-at-liu/vacancies/27140)
- **Department:** 
- **Published:** 
- **Deadline:** 2025-10-01

</div>

<div class="job" data-type="Postdoc/Researcher" style="margin-bottom: 1.5em;">
<h3>Postdoc in Computational Social Science</h3>

- **Link:** [View job posting](https://liu.se/en/work-at-liu/vacancies/27207)
- **Department:** 
- **Published:** 
- **Deadline:** 2025-09-30

</div>

<div class="job" data-type="Postdoc/Researcher" style="margin-bottom: 1.5em;">
<h3>Postdoc in Computational Social Science</h3>

- **Link:** [View job posting](https://liu.se/en/work-at-liu/vacancies/27295)
- **Department:** 
- **Published:** 
- **Deadline:** 2025-09-30

</div>

<div class="job" data-type="Postdoc/Researcher" style="margin-bottom: 1.5em;">
<h3>Postdoc in organic bioelectronics</h3>

- **Link:** [View job posting](https://liu.se/en/work-at-liu/vacancies/27344)
- **Department:** 
- **Published:** 
- **Deadline:** 2025-09-12

</div>

<div class="job" data-type="PhD" style="margin-bottom: 1.5em;">
<h3>PhD student in Environmental Science at Environmental Change</h3>

- **Link:** [View job posting](https://liu.se/en/work-at-liu/vacancies/27133)
- **Department:** 
- **Published:** 
- **Deadline:** 2025-09-08

</div>

<div class="job" data-type="PhD" style="margin-bottom: 1.5em;">
<h3>PhD Student in Reinforcement Learning for Control of Partially Observable Dynamical Systems</h3>

- **Link:** [View job posting](https://liu.se/en/work-at-liu/vacancies/27355)
- **Department:** 
- **Published:** 
- **Deadline:** 2025-09-05

</div>

<div class="job" data-type="Other" style="margin-bottom: 1.5em;">
<h3>Teaching assistants/Amanuens in Fluid and Mechatronic systems</h3>

- **Link:** [View job posting](https://liu.se/en/work-at-liu/vacancies/27365)
- **Department:** 
- **Published:** 
- **Deadline:** 2025-09-04

</div>

<div class="job" data-type="PhD" style="margin-bottom: 1.5em;">
<h3>PhD student in Analytical Sociology</h3>

- **Link:** [View job posting](https://liu.se/en/work-at-liu/vacancies/27064)
- **Department:** 
- **Published:** 
- **Deadline:** 2025-08-31

</div>

<div class="job" data-type="Other" style="margin-bottom: 1.5em;">
<h3>Teaching assistants/Amanuens in Applied Thermodynamics and Fluid Mechanics</h3>

- **Link:** [View job posting](https://liu.se/en/work-at-liu/vacancies/27373)
- **Department:** 
- **Published:** 
- **Deadline:** 2025-08-31

</div>

<div class="job" data-type="Other" style="margin-bottom: 1.5em;">
<h3>International student ambassador</h3>

- **Link:** [View job posting](https://liu.se/en/work-at-liu/vacancies/27177)
- **Department:** 
- **Published:** 
- **Deadline:** 2025-08-30

</div>

<div class="job" data-type="Lecturer/Professor" style="margin-bottom: 1.5em;">
<h3>Assistant Professor in Materials Science with a focus on simulation and modeling of organic functional materials for sustainability</h3>

- **Link:** [View job posting](https://liu.se/en/work-at-liu/vacancies/27194)
- **Department:** 
- **Published:** 
- **Deadline:** 2025-08-29

</div>

<div class="job" data-type="PhD" style="margin-bottom: 1.5em;">
<h3>PhD student in Scientific Visualization</h3>

- **Link:** [View job posting](https://liu.se/en/work-at-liu/vacancies/27223)
- **Department:** 
- **Published:** 
- **Deadline:** 2025-08-29

</div>

<div class="job" data-type="Lecturer/Professor" style="margin-bottom: 1.5em;">
<h3>Assistant professor in Machine Learning with a focus on Computational Photography</h3>

- **Link:** [View job posting](https://liu.se/en/work-at-liu/vacancies/27224)
- **Department:** 
- **Published:** 
- **Deadline:** 2025-08-25

</div>

<div class="job" data-type="Other" style="margin-bottom: 1.5em;">
<h3>Systems Developer Linux / Devops at AIDA Data Hub</h3>

- **Link:** [View job posting](https://liu.se/en/work-at-liu/vacancies/27193)
- **Department:** 
- **Published:** 
- **Deadline:** 2025-08-24

</div>

<div class="job" data-type="PhD" style="margin-bottom: 1.5em;">
<h3>PhD student in Theoretical Ecology</h3>

- **Link:** [View job posting](https://liu.se/en/work-at-liu/vacancies/27211)
- **Department:** 
- **Published:** 
- **Deadline:** 2025-08-22
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
