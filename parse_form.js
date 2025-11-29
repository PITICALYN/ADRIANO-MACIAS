const fs = require('fs');

const html = fs.readFileSync('google_form_full.html', 'utf8');
const match = html.match(/var FB_PUBLIC_LOAD_DATA_ = (\[.+?\]);\s*<\/script>/);

if (match) {
    const data = JSON.parse(match[1]);
    const questions = data[1][1];

    questions.forEach(q => {
        const title = q[1];
        const entryId = q[4][0][0];
        const options = q[4][0][1];

        console.log(`Title: ${title}`);
        console.log(`ID: ${entryId}`);
        if (options) {
            console.log('Options:');
            options.forEach(o => console.log(`  - "${o[0]}"`));
        } else {
            console.log('Type: Text/Other');
        }
        console.log('---');
    });
} else {
    console.log('Could not find FB_PUBLIC_LOAD_DATA_');
}
