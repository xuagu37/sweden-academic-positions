# Malmö University
<p style="font-size: 1.2em; font-weight: bold;">Total positions: 7</p>


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
<h3>Research Assistant in AIoT-Integrated Electronic Tongue Prototype for Saliva Diagnostics</h3>

- **Link:** [View job posting](https://web103.reachmee.com/ext/I005/1015/job?site=7&lang=UK&validator=e5819a4704cd849685049472c0c17895&job_id=4203)
- **Department:** Faculty of technology and society
- **Published:** 12 September 2025
- **Deadline:** 26 September 2025

</div>

<div class="job" data-type="Other" style="margin-bottom: 1.5em;">
<h3>Student Assistant for the International Office</h3>

- **Link:** [View job posting](https://web103.reachmee.com/ext/I005/1015/job?site=7&lang=UK&validator=e5819a4704cd849685049472c0c17895&job_id=4197)
- **Department:** -
- **Published:** 11 September 2025
- **Deadline:** 25 September 2025

</div>

<div class="job" data-type="PhD" style="margin-bottom: 1.5em;">
<h3>Employment as a doctoral student in Urban Studies focused on Digital Innovation and the Sustainable Built Environment</h3>

- **Link:** [View job posting](https://web103.reachmee.com/ext/I005/1015/job?site=7&lang=UK&validator=e5819a4704cd849685049472c0c17895&job_id=4192)
- **Department:** Faculty of culture and society  / Department of Urban Studies
- **Published:** 09 September 2025
- **Deadline:** 12 October 2025

</div>

<div class="job" data-type="PhD" style="margin-bottom: 1.5em;">
<h3>Employment as a doctoral student in computer Science: Data-driven product development, evolution and management</h3>

- **Link:** [View job posting](https://web103.reachmee.com/ext/I005/1015/job?site=7&lang=UK&validator=e5819a4704cd849685049472c0c17895&job_id=4186)
- **Department:** Faculty of technology and society
- **Published:** 05 September 2025
- **Deadline:** 10 October 2025

</div>

<div class="job" data-type="Postdoc/Researcher" style="margin-bottom: 1.5em;">
<h3>Project researcher in Biomedical science with focus on Cardiovascular Disease</h3>

- **Link:** [View job posting](https://web103.reachmee.com/ext/I005/1015/job?site=7&lang=UK&validator=e5819a4704cd849685049472c0c17895&job_id=4171)
- **Department:** Faculty of health and society  / Department of Biomedical Science
- **Published:** 25 August 2025
- **Deadline:** 30 September 2025

</div>

<div class="job" data-type="Other" style="margin-bottom: 1.5em;">
<h3>Part-Time Research Assistant in Interpretable Machine Learning (5-Month Duration)</h3>

- **Link:** [View job posting](https://web103.reachmee.com/ext/I005/1015/job?site=7&lang=UK&validator=e5819a4704cd849685049472c0c17895&job_id=4160)
- **Department:** Faculty of technology and society
- **Published:** 13 August 2025
- **Deadline:** 23 September 2025

</div>

<div class="job" data-type="Other" style="margin-bottom: 1.5em;">
<h3>Part-Time Research Assistant in Interpretable Machine Learning (11-Month Duration)"</h3>

- **Link:** [View job posting](https://web103.reachmee.com/ext/I005/1015/job?site=7&lang=UK&validator=e5819a4704cd849685049472c0c17895&job_id=4132)
- **Department:** Faculty of technology and society
- **Published:** 30 June 2025
- **Deadline:** 23 September 2025
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
