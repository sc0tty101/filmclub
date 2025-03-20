import Airtable from 'airtable';

// Fetch data from Airtable at build time using getStaticProps
export async function getStaticProps() {
  // Configure Airtable using environment variables
  const base = new Airtable({ apiKey: process.env.AIRTABLE_API_KEY })
    .base(process.env.AIRTABLE_BASE_ID);
  
  // Retrieve records from the "WEEKS" table
  const records = await base('WEEKS').select({}).firstPage();

  // Map records to a simpler object structure
  const weeks = records.map(record => ({
    id: record.id,
    ...record.fields
  }));

  return {
    props: {
      weeks,
    },
    // Optional: Rebuild the page every 10 seconds for new data
    revalidate: 10,
  };
}

const HomePage = ({ weeks }) => {
  return (
    <div>
      <h1>Film Club Weeks</h1>
      <ul>
        {weeks.map(week => (
          <li key={week.id}>
            {week.name ? week.name : 'Unnamed Week'}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default HomePage;
