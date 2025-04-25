# Luleå University
<p style="font-size: 1.2em; font-weight: bold;">Total positions: 14</p>


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
<h3>Professor/Head of Subject of Construction Management and Building Technology</h3>

- **Link:** [View job posting](https://www.ltu.se/en/about-ltu/work-at-ltu/vacant-positions#item-8855)
- **Department:** 
- **Published:** 
- **Deadline:** 2025-04-28

</div>

<div class="job" data-type="Other" style="margin-bottom: 1.5em;">
<h3>Ph.D. Position in ‘Valorization of Industrial Waste Streams for Sustainable Metal Recovery in a Circular Economy’.</h3>

- **Link:** [View job posting](https://www.ltu.se/en/about-ltu/work-at-ltu/vacant-positions#item-8996)
- **Department:** 
- **Published:** 
- **Deadline:** 2025-04-30

</div>

<div class="job" data-type="PhD" style="margin-bottom: 1.5em;">
<h3>PhD in Machine Elements on Polymer Liner applicaton in hydrogen storage</h3>

- **Link:** [View job posting](https://www.ltu.se/en/about-ltu/work-at-ltu/vacant-positions#item-8957)
- **Department:** 
- **Published:** 
- **Deadline:** 2025-04-30

</div>

<div class="job" data-type="Lecturer/Professor" style="margin-bottom: 1.5em;">
<h3>Senior Lecturer in Building Materials</h3>

- **Link:** [View job posting](https://www.ltu.se/en/about-ltu/work-at-ltu/vacant-positions#item-9005)
- **Department:** 
- **Published:** 
- **Deadline:** 2025-04-30

</div>

<div class="job" data-type="PhD" style="margin-bottom: 1.5em;">
<h3>PhD student in Robotics and Artificial Intelligence WASP</h3>

- **Link:** [View job posting](https://www.ltu.se/en/about-ltu/work-at-ltu/vacant-positions#item-8982)
- **Department:** 
- **Published:** 
- **Deadline:** 2025-05-02

</div>

<div class="job" data-type="PhD" style="margin-bottom: 1.5em;">
<h3>PhD student in Robotics and Artificial Intelligence WASP</h3>

- **Link:** [View job posting](https://www.ltu.se/en/about-ltu/work-at-ltu/vacant-positions#item-8986)
- **Department:** 
- **Published:** 
- **Deadline:** 2025-05-02

</div>

<div class="job" data-type="Postdoc/Researcher" style="margin-bottom: 1.5em;">
<h3>Postdoc position in Robotics and Artificial Intelligence WASP</h3>

- **Link:** [View job posting](https://www.ltu.se/en/about-ltu/work-at-ltu/vacant-positions#item-8991)
- **Department:** 
- **Published:** 
- **Deadline:** 2025-05-02

</div>

<div class="job" data-type="Postdoc/Researcher" style="margin-bottom: 1.5em;">
<h3>Postdoc position in Robotics and Artificial Intelligence WASP</h3>

- **Link:** [View job posting](https://www.ltu.se/en/about-ltu/work-at-ltu/vacant-positions#item-8993)
- **Department:** 
- **Published:** 
- **Deadline:** 2025-05-02

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

<div class="job" data-type="Other" style="margin-bottom: 1.5em;">
<h3>Summer student in Cyber-Physical Systems</h3>

- **Link:** [View job posting](https://www.ltu.se/en/about-ltu/work-at-ltu/vacant-positions#item-9073)
- **Department:** 
- **Published:** 
- **Deadline:** 2025-05-25

</div>

<div class="job" data-type="Lecturer/Professor" style="margin-bottom: 1.5em;">
<h3>​​Professor/Head of Subject of Cyber-Physical Systems​</h3>

- **Link:** [View job posting](https://www.ltu.se/en/about-ltu/work-at-ltu/vacant-positions#item-8922)
- **Department:** 
- **Published:** 
- **Deadline:** 2025-05-31
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
