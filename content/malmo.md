# Malmö University
<p style="font-size: 1.2em; font-weight: bold;">Total positions: 4</p>


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

<div class="job" data-type="Postdoc/Researcher" style="margin-bottom: 1.5em;">
<h3>Short-time Research Fellow (Project Researcher) at  Russia, Ukraine and the Caucasus Regional Research</h3>

- **Link:** [View job posting](https://web103.reachmee.com/ext/I005/1015/job?site=7&lang=UK&validator=e5819a4704cd849685049472c0c17895&job_id=4149)
- **Department:** Faculty of culture and society  / Department of Global Political Studies
- **Published:** 16 July 2025
- **Deadline:** 15 August 2025

</div>

<div class="job" data-type="Lecturer/Professor" style="margin-bottom: 1.5em;">
<h3>Senior Lecturer in Industrial Product Development</h3>

- **Link:** [View job posting](https://web103.reachmee.com/ext/I005/1015/job?site=7&lang=UK&validator=e5819a4704cd849685049472c0c17895&job_id=4089)
- **Department:** Faculty of technology and society
- **Published:** 02 July 2025
- **Deadline:** 31 August 2025

</div>

<div class="job" data-type="Other" style="margin-bottom: 1.5em;">
<h3>Teaching Assistant in the IOIO Mechatronics Lab</h3>

- **Link:** [View job posting](https://web103.reachmee.com/ext/I005/1015/job?site=7&lang=UK&validator=e5819a4704cd849685049472c0c17895&job_id=4141)
- **Department:** Faculty of culture and society  / School of Arts and Communication
- **Published:** 01 July 2025
- **Deadline:** 17 August 2025

</div>

<div class="job" data-type="Other" style="margin-bottom: 1.5em;">
<h3>Research Assistant in Interpretable Machine Learning</h3>

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
