# Malmö University
<p style="font-size: 1.2em; font-weight: bold;">Total positions: 3</p>


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
<h3>Research Assistant in responsible AI for education and mobility</h3>

- **Link:** [View job posting](https://web103.reachmee.com/ext/I005/1015/job?site=7&lang=UK&validator=e5819a4704cd849685049472c0c17895&job_id=4104)
- **Department:** Faculty of technology and society
- **Published:** 16 June 2025
- **Deadline:** 30 June 2025

</div>

<div class="job" data-type="Other" style="margin-bottom: 1.5em;">
<h3>Research Assistant in IoT and Human-Machine Interaction</h3>

- **Link:** [View job posting](https://web103.reachmee.com/ext/I005/1015/job?site=7&lang=UK&validator=e5819a4704cd849685049472c0c17895&job_id=4094)
- **Department:** Faculty of technology and society
- **Published:** 09 June 2025
- **Deadline:** 15 July 2025

</div>

<div class="job" data-type="Other" style="margin-bottom: 1.5em;">
<h3>Research Assistant in pedagogical research and educational innovation</h3>

- **Link:** [View job posting](https://web103.reachmee.com/ext/I005/1015/job?site=7&lang=UK&validator=e5819a4704cd849685049472c0c17895&job_id=4097)
- **Department:** Faculty of technology and society
- **Published:** 09 June 2025
- **Deadline:** 15 July 2025
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
