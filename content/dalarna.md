# Dalarna University
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

<div class="job" data-type="Other" style="margin-bottom: 1.5em;">
<h3>Universitetslektor i bild/bilddidaktik</h3>

- **Link:** [View job posting](https://www.du.se/en/about-du/career-opportunities/vacant-positions/vacant-position/?job=2538)
- **Department:** 
- **Published:** 
- **Deadline:** 5/30/2025

</div>

<div class="job" data-type="Other" style="margin-bottom: 1.5em;">
<h3>Universitetsadjunkt i bild/bilddidaktik</h3>

- **Link:** [View job posting](https://www.du.se/en/about-du/career-opportunities/vacant-positions/vacant-position/?job=2539)
- **Department:** 
- **Published:** 
- **Deadline:** 5/30/2025

</div>

<div class="job" data-type="Other" style="margin-bottom: 1.5em;">
<h3>Kommunikatör</h3>

- **Link:** [View job posting](https://www.du.se/en/about-du/career-opportunities/vacant-positions/vacant-position/?job=2579)
- **Department:** 
- **Published:** 
- **Deadline:** 6/1/2025

</div>

<div class="job" data-type="Other" style="margin-bottom: 1.5em;">
<h3>Universitetsadjunkt i italienska 25%</h3>

- **Link:** [View job posting](https://www.du.se/en/about-du/career-opportunities/vacant-positions/vacant-position/?job=2564)
- **Department:** 
- **Published:** 
- **Deadline:** 6/2/2025

</div>

<div class="job" data-type="Other" style="margin-bottom: 1.5em;">
<h3>Doktorand i vårdvetenskap:  Bildskapande interventioner till ungdomar</h3>

- **Link:** [View job posting](https://www.du.se/en/about-du/career-opportunities/vacant-positions/vacant-position/?job=2576)
- **Department:** 
- **Published:** 
- **Deadline:** 6/2/2025
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
