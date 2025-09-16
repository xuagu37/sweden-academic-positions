# Luleå University
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

</div>

<div class="job" data-type="Research Engineer" style="margin-bottom: 1.5em;">
<h3>Senior Research Engineer to Dependable Communications and Computations</h3>

- **Link:** [View job posting](https://www.ltu.se/en/about-ltu/work-at-ltu/vacant-positions#item-9403)
- **Department:** 
- **Published:** 
- **Deadline:** 2025-09-23

</div>

<div class="job" data-type="Postdoc/Researcher" style="margin-bottom: 1.5em;">
<h3>Postdoc position in Product Innovation</h3>

- **Link:** [View job posting](https://www.ltu.se/en/about-ltu/work-at-ltu/vacant-positions#item-9428)
- **Department:** 
- **Published:** 
- **Deadline:** 2025-09-25

</div>

<div class="job" data-type="Postdoc/Researcher" style="margin-bottom: 1.5em;">
<h3>Postdoc position in Robotics and Artificial Intelligence</h3>

- **Link:** [View job posting](https://www.ltu.se/en/about-ltu/work-at-ltu/vacant-positions#item-9390)
- **Department:** 
- **Published:** 
- **Deadline:** 2025-09-26

</div>

<div class="job" data-type="Postdoc/Researcher" style="margin-bottom: 1.5em;">
<h3>Postdoc position in Robotics and Artificial Intelligence WASP</h3>

- **Link:** [View job posting](https://www.ltu.se/en/about-ltu/work-at-ltu/vacant-positions#item-9394)
- **Department:** 
- **Published:** 
- **Deadline:** 2025-09-26

</div>

<div class="job" data-type="PhD" style="margin-bottom: 1.5em;">
<h3>PhD Student in Building Materials</h3>

- **Link:** [View job posting](https://www.ltu.se/en/about-ltu/work-at-ltu/vacant-positions#item-9396)
- **Department:** 
- **Published:** 
- **Deadline:** 2025-09-30

</div>

<div class="job" data-type="PhD" style="margin-bottom: 1.5em;">
<h3>PhD-student position in Energy Engineering – with a special emphasis on electro-conversion of lignin and its derivatives for bio-chemical production</h3>

- **Link:** [View job posting](https://www.ltu.se/en/about-ltu/work-at-ltu/vacant-positions#item-9422)
- **Department:** 
- **Published:** 
- **Deadline:** 2025-10-02
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
