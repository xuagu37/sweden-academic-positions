# Luleå University
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

<div class="job" data-type="PhD" style="margin-bottom: 1.5em;">
<h3>PhD Student in Structural Engineering</h3>

- **Link:** [View job posting](https://www.ltu.se/en/about-ltu/work-at-ltu/vacant-positions#item-9223)
- **Department:** 
- **Published:** 
- **Deadline:** 2025-08-10

</div>

<div class="job" data-type="Postdoc/Researcher" style="margin-bottom: 1.5em;">
<h3>Postdoc position in Structural Engineering</h3>

- **Link:** [View job posting](https://www.ltu.se/en/about-ltu/work-at-ltu/vacant-positions#item-9245)
- **Department:** 
- **Published:** 
- **Deadline:** 2025-08-10

</div>

<div class="job" data-type="PhD" style="margin-bottom: 1.5em;">
<h3>PhD student in Robotics and Artificial Intelligence WASP</h3>

- **Link:** [View job posting](https://www.ltu.se/en/about-ltu/work-at-ltu/vacant-positions#item-9288)
- **Department:** 
- **Published:** 
- **Deadline:** 2025-08-15

</div>

<div class="job" data-type="Postdoc/Researcher" style="margin-bottom: 1.5em;">
<h3>Postdoctoral in Signal Processing: Acoustic Backscatter Communications</h3>

- **Link:** [View job posting](https://www.ltu.se/en/about-ltu/work-at-ltu/vacant-positions#item-9204)
- **Department:** 
- **Published:** 
- **Deadline:** 2025-08-15

</div>

<div class="job" data-type="Postdoc/Researcher" style="margin-bottom: 1.5em;">
<h3>Postdoctor in Mining and Rock Engineering- “Improvement of loading and transportation system in SLC-mines.”</h3>

- **Link:** [View job posting](https://www.ltu.se/en/about-ltu/work-at-ltu/vacant-positions#item-9274)
- **Department:** 
- **Published:** 
- **Deadline:** 2025-08-15

</div>

<div class="job" data-type="PhD" style="margin-bottom: 1.5em;">
<h3>PhD Student in Machine Learning</h3>

- **Link:** [View job posting](https://www.ltu.se/en/about-ltu/work-at-ltu/vacant-positions#item-9314)
- **Department:** 
- **Published:** 
- **Deadline:** 2025-08-17

</div>

<div class="job" data-type="Research Engineer" style="margin-bottom: 1.5em;">
<h3>Senior Research Engineer in Robotics and Artificial Intelligence</h3>

- **Link:** [View job posting](https://www.ltu.se/en/about-ltu/work-at-ltu/vacant-positions#item-9331)
- **Department:** 
- **Published:** 
- **Deadline:** 2025-08-17

</div>

<div class="job" data-type="PhD" style="margin-bottom: 1.5em;">
<h3>PhD Student in Space Systems</h3>

- **Link:** [View job posting](https://www.ltu.se/en/about-ltu/work-at-ltu/vacant-positions#item-9322)
- **Department:** 
- **Published:** 
- **Deadline:** 2025-08-24

</div>

<div class="job" data-type="PhD" style="margin-bottom: 1.5em;">
<h3>PhD Student in hydrometallurgical extraction of critical raw material</h3>

- **Link:** [View job posting](https://www.ltu.se/en/about-ltu/work-at-ltu/vacant-positions#item-9231)
- **Department:** 
- **Published:** 
- **Deadline:** 2025-09-01

</div>

<div class="job" data-type="PhD" style="margin-bottom: 1.5em;">
<h3>PhD Student in Urban Water Engineering – pollutant processes in nature-based stormwater systems</h3>

- **Link:** [View job posting](https://www.ltu.se/en/about-ltu/work-at-ltu/vacant-positions#item-9227)
- **Department:** 
- **Published:** 
- **Deadline:** 2025-09-05

</div>

<div class="job" data-type="Lecturer/Professor" style="margin-bottom: 1.5em;">
<h3>WISE Fellow Senior Lecturer in Composite Materials</h3>

- **Link:** [View job posting](https://www.ltu.se/en/about-ltu/work-at-ltu/vacant-positions#item-9189)
- **Department:** 
- **Published:** 
- **Deadline:** 2025-09-21

</div>

<div class="job" data-type="Lecturer/Professor" style="margin-bottom: 1.5em;">
<h3>WISE Fellow Senior Lecturer in Experimental Physics</h3>

- **Link:** [View job posting](https://www.ltu.se/en/about-ltu/work-at-ltu/vacant-positions#item-9216)
- **Department:** 
- **Published:** 
- **Deadline:** 2025-09-21
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
