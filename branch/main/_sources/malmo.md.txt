# Malmö University
<p style="font-size: 1.2em; font-weight: bold;">Total positions: 8</p>


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
<h3>Employment as a doctoral student in International Migration and Ethnic Relations (IMER) within the ERC Starting Grant project Give Rights</h3>

- **Link:** [View job posting](https://web103.reachmee.com/ext/I005/1015/job?site=7&lang=UK&validator=e5819a4704cd849685049472c0c17895&job_id=4334)
- **Department:** Faculty of culture and society  / Department of Global Political Studies
- **Published:** 10 December 2025
- **Deadline:** 18 January 2026

</div>

<div class="job" data-type="Other" style="margin-bottom: 1.5em;">
<h3>Research Assistant in Trustworthy Large Language Models for Mobility</h3>

- **Link:** [View job posting](https://web103.reachmee.com/ext/I005/1015/job?site=7&lang=UK&validator=e5819a4704cd849685049472c0c17895&job_id=4321)
- **Department:** Faculty of technology and society
- **Published:** 27 November 2025
- **Deadline:** 18 December 2025

</div>

<div class="job" data-type="PhD" style="margin-bottom: 1.5em;">
<h3>Employment as a PhD student in Odontology</h3>

- **Link:** [View job posting](https://web103.reachmee.com/ext/I005/1015/job?site=7&lang=UK&validator=e5819a4704cd849685049472c0c17895&job_id=4308)
- **Department:** Faculty of odontology  / Sektion 1
- **Published:** 20 November 2025
- **Deadline:** 31 December 2025

</div>

<div class="job" data-type="PhD" style="margin-bottom: 1.5em;">
<h3>PhD student in Education with focus on school leadership</h3>

- **Link:** [View job posting](https://web103.reachmee.com/ext/I005/1015/job?site=7&lang=UK&validator=e5819a4704cd849685049472c0c17895&job_id=4303)
- **Department:** Faculty of education and society  / Departments of School development and Leadership
- **Published:** 19 November 2025
- **Deadline:** 30 January 2026

</div>

<div class="job" data-type="PhD" style="margin-bottom: 1.5em;">
<h3>PhD student in education with focus on special education in one of the educational system's school forms</h3>

- **Link:** [View job posting](https://web103.reachmee.com/ext/I005/1015/job?site=7&lang=UK&validator=e5819a4704cd849685049472c0c17895&job_id=4305)
- **Department:** Faculty of education and society  / Departments of School development and Leadership
- **Published:** 19 November 2025
- **Deadline:** 30 January 2026

</div>

<div class="job" data-type="PhD" style="margin-bottom: 1.5em;">
<h3>Doctoral students in Sport Science specialising in social sciences and the humanities</h3>

- **Link:** [View job posting](https://web103.reachmee.com/ext/I005/1015/job?site=7&lang=UK&validator=e5819a4704cd849685049472c0c17895&job_id=4294)
- **Department:** Faculty of education and society  / Department of Sport Science - Sport and Leisure
- **Published:** 14 November 2025
- **Deadline:** 20 January 2026

</div>

<div class="job" data-type="PhD" style="margin-bottom: 1.5em;">
<h3>Doctoral students in mathematics and science education</h3>

- **Link:** [View job posting](https://web103.reachmee.com/ext/I005/1015/job?site=7&lang=UK&validator=e5819a4704cd849685049472c0c17895&job_id=4298)
- **Department:** Faculty of education and society  / Instutitionen för natur-matematik-samhälle
- **Published:** 14 November 2025
- **Deadline:** 20 January 2026

</div>

<div class="job" data-type="PhD" style="margin-bottom: 1.5em;">
<h3>Employment as a doctoral student in Global politics</h3>

- **Link:** [View job posting](https://web103.reachmee.com/ext/I005/1015/job?site=7&lang=UK&validator=e5819a4704cd849685049472c0c17895&job_id=4243)
- **Department:** Faculty of culture and society  / Department of Global Political Studies
- **Published:** 03 November 2025
- **Deadline:** 31 January 2026
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
