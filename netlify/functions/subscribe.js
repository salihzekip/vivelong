/* Brevo (Sendinblue) e-posta aboneliği
   Netlify Environment Variables'a şunları ekleyin:
   - BREVO_API_KEY: Brevo'dan aldığınız API anahtarı
   - BREVO_LIST_ID: Abonelerin ekleneceği liste ID'si (varsayılan: 2)
*/
exports.handler = async (event) => {
  if (event.httpMethod !== 'POST') {
    return { statusCode: 405, body: 'Method Not Allowed' };
  }

  let body;
  try { body = JSON.parse(event.body); }
  catch { return { statusCode: 400, body: 'Invalid JSON' }; }

  const { email, firstName } = body;
  if (!email) return { statusCode: 400, body: 'Email required' };

  const apiKey = process.env.BREVO_API_KEY;
  const listId = parseInt(process.env.BREVO_LIST_ID || '2');

  if (!apiKey) {
    return { statusCode: 500, body: 'BREVO_API_KEY not configured' };
  }

  try {
    const res = await fetch('https://api.brevo.com/v3/contacts', {
      method: 'POST',
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api-key': apiKey
      },
      body: JSON.stringify({
        email,
        attributes: { FIRSTNAME: firstName || '' },
        listIds: [listId],
        updateEnabled: true
      })
    });

    const data = await res.json();
    return {
      statusCode: res.ok ? 200 : 400,
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(data)
    };
  } catch (err) {
    return { statusCode: 500, body: 'Internal error: ' + err.message };
  }
};
