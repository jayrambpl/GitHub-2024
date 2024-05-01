import requests

def get_github_repositories(organization_name):
    base_url = f'https://api.github.com/users/{organization_name}/repos'
    
    try:
        response = requests.get(base_url)
        response.raise_for_status()  # Check for errors in the HTTP response
        repositories = response.json()
        # Extract repository names
        repo_data = [{'name': repo['name'], 'branches_url': repo['branches_url']} for repo in repositories]
        
        return repo_data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching repositories: {e}")
        return []

def get_repository_branches(branches_url):
    try:
        response = requests.get(branches_url)
        response.raise_for_status()  # Check for errors in the HTTP response
        branches = response.json()
        
        # Extract branch names
        branch_names = [branch['name'] for branch in branches]
        
        return branch_names
    except requests.exceptions.RequestException as e:
        print(f"Error fetching branches: {e}")
        return []

if __name__ == "__main__":
    organization_name = "jayrambpl"
    
    repositories = get_github_repositories(organization_name)
    
    if repositories:
        print(f"Repositories in {organization_name} organization:")
        for repo_data in repositories:
            repo_name = repo_data['name']
            branches_url = repo_data['branches_url'].replace('{/branch}', '')  # Remove placeholder
            
            print(f"\nBranches for {repo_name}:")
            branches = get_repository_branches(branches_url)
            for branch in branches:
                print(branch)
    else:
        print(f"No repositories found for {organization_name}.")
# ------------------