# Luleå University
<p style="font-size: 1.2em; font-weight: bold;">Total positions: 13</p>


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
<h3>Postdoctoral position in Computational and Applied Geophysics</h3>

- **Link:** [View job posting](https://www.ltu.se/en/about-ltu/work-at-ltu/vacant-positions#item-9570)
- **Department:** 
- **Published:** 
- **Deadline:** 

</div>

<div class="job" data-type="Postdoc/Researcher" style="margin-bottom: 1.5em;">
<h3>Postdoc position in applied geophysics (magnetotellurics)</h3>

- **Link:** [View job posting](https://www.ltu.se/en/about-ltu/work-at-ltu/vacant-positions#item-9576)
- **Department:** 
- **Published:** 
- **Deadline:** 

</div>

<div class="job" data-type="Lecturer/Professor" style="margin-bottom: 1.5em;">
<h3>Associate Senior Lecturer in Experimental Mechanics</h3>

- **Link:** [View job posting](https://www.ltu.se/en/about-ltu/work-at-ltu/vacant-positions#item-9607)
- **Department:** 
- **Published:** 
- **Deadline:** 

</div>

<div class="job" data-type="Postdoc/Researcher" style="margin-bottom: 1.5em;">
<h3>Postdoctor position in Architecture</h3>

- **Link:** [View job posting](https://www.ltu.se/en/about-ltu/work-at-ltu/vacant-positions#item-9645)
- **Department:** 
- **Published:** 
- **Deadline:** 

</div>

<div class="job" data-type="PhD" style="margin-bottom: 1.5em;">
<h3>PhD Student in Cybersecurity with Specialization in IT/OT Security</h3>

- **Link:** [View job posting](https://www.ltu.se/en/about-ltu/work-at-ltu/vacant-positions#item-9679)
- **Department:** 
- **Published:** 
- **Deadline:** 

</div>

<div class="job" data-type="Lecturer/Professor" style="margin-bottom: 1.5em;">
<h3>Senior Lecturer in Process Metallurgy with specialisation in Hydrometallurgy</h3>

- **Link:** [View job posting](https://www.ltu.se/en/about-ltu/work-at-ltu/vacant-positions#item-9568)
- **Department:** 
- **Published:** 
- **Deadline:** 

</div>

<div class="job" data-type="PhD" style="margin-bottom: 1.5em;">
<h3>PhD positions in Signal Processing: 6G space-terrestrial communications and sensing</h3>

- **Link:** [View job posting](https://www.ltu.se/en/about-ltu/work-at-ltu/vacant-positions#item-9586)
- **Department:** 
- **Published:** 
- **Deadline:** 

</div>

<div class="job" data-type="PhD" style="margin-bottom: 1.5em;">
<h3>PhD Student in Mineral Processing</h3>

- **Link:** [View job posting](https://www.ltu.se/en/about-ltu/work-at-ltu/vacant-positions#item-9655)
- **Department:** 
- **Published:** 
- **Deadline:** 

</div>

<div class="job" data-type="Postdoc/Researcher" style="margin-bottom: 1.5em;">
<h3>Postdoctoral position in Mineral Processing</h3>

- **Link:** [View job posting](https://www.ltu.se/en/about-ltu/work-at-ltu/vacant-positions#item-9656)
- **Department:** 
- **Published:** 
- **Deadline:** 

</div>

<div class="job" data-type="Postdoc/Researcher" style="margin-bottom: 1.5em;">
<h3>Postdoctoral position in ore geology</h3>

- **Link:** [View job posting](https://www.ltu.se/en/about-ltu/work-at-ltu/vacant-positions#item-9683)
- **Department:** 
- **Published:** 
- **Deadline:** 

</div>

<div class="job" data-type="PhD" style="margin-bottom: 1.5em;">
<h3>PhD Student in Robotics and Artificial Intelligence</h3>

- **Link:** [View job posting](https://www.ltu.se/en/about-ltu/work-at-ltu/vacant-positions#item-9698)
- **Department:** 
- **Published:** 
- **Deadline:** 

</div>

<div class="job" data-type="Lecturer/Professor" style="margin-bottom: 1.5em;">
<h3>Associate Senior Lecturer in Automatic Control</h3>

- **Link:** [View job posting](https://www.ltu.se/en/about-ltu/work-at-ltu/vacant-positions#item-9662)
- **Department:** 
- **Published:** 
- **Deadline:** 

</div>

<div class="job" data-type="Lecturer/Professor" style="margin-bottom: 1.5em;">
<h3>Professor/Head of Subject of Fire Technology</h3>

- **Link:** [View job posting](https://www.ltu.se/en/about-ltu/work-at-ltu/vacant-positions#item-9701)
- **Department:** 
- **Published:** 
- **Deadline:**
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
