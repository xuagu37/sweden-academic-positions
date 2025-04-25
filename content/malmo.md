# Malmö University
<p style="font-size: 1.2em; font-weight: bold;">Total positions: 5</p>


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
<h3>PhD project: Electrochemical Investigation of Nanostructured Surfaces for Biosensing Applications in Oral Diagnostics</h3>

- **Link:** [View job posting](http://web103.reachmee.com/ext/I005/1015/job?site=7&lang=UK&validator=e5819a4704cd849685049472c0c17895&job_id=3993)
- **Department:** Faculty of health and society  / Department of Biomedical Science
- **Published:** 17 April 2025
- **Deadline:** 09 May 2025

</div>

<div class="job" data-type="PhD" style="margin-bottom: 1.5em;">
<h3>Doctoral student in IMER with a focus on survey studies of diversity and inclusion</h3>

- **Link:** [View job posting](http://web103.reachmee.com/ext/I005/1015/job?site=7&lang=UK&validator=e5819a4704cd849685049472c0c17895&job_id=3963)
- **Department:** Faculty of culture and society  / Department of Global Political Studies
- **Published:** 03 April 2025
- **Deadline:** 04 May 2025

</div>

<div class="job" data-type="Postdoc/Researcher" style="margin-bottom: 1.5em;">
<h3>Postdoctoral Researcher in Molecular Dynamics Simulations of Water and Hydration</h3>

- **Link:** [View job posting](http://web103.reachmee.com/ext/I005/1015/job?site=7&lang=UK&validator=e5819a4704cd849685049472c0c17895&job_id=3957)
- **Department:** Faculty of health and society  / Department of Biomedical Science
- **Published:** 02 April 2025
- **Deadline:** 01 May 2025

</div>

<div class="job" data-type="PhD" style="margin-bottom: 1.5em;">
<h3>PhD project: Development of non-invasive analytics for monitoring host-microbiota interplay</h3>

- **Link:** [View job posting](http://web103.reachmee.com/ext/I005/1015/job?site=7&lang=UK&validator=e5819a4704cd849685049472c0c17895&job_id=3950)
- **Department:** Malmö universitet  / Malmö universitet
- **Published:** 28 March 2025
- **Deadline:** 22 May 2025

</div>

<div class="job" data-type="Lecturer/Professor" style="margin-bottom: 1.5em;">
<h3>Professor in Surface Chemistry with Focus on Studies of Biointerfaces</h3>

- **Link:** [View job posting](http://web103.reachmee.com/ext/I005/1015/job?site=7&lang=UK&validator=e5819a4704cd849685049472c0c17895&job_id=3928)
- **Department:** Faculty of health and society  / Department of Biomedical Science
- **Published:** 12 March 2025
- **Deadline:** 30 April 2025
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
