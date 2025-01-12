printf 'Change folder...'
cd ..

printf 'Update assets...'
briefcase update --update-resources

printf 'Create build template...'
briefcase create

printf 'Build...'
briefcase build

printf 'Run...'
briefcase run