"""Tests for the release notes generation script."""

import sys
import os
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '01-release-notes-automation'))

from generate_release_notes import (
    get_sample_commits,
    generate_release_notes,
    fetch_commits,
)


class TestGetSampleCommits:
    def test_returns_list(self):
        commits = get_sample_commits()
        assert isinstance(commits, list)

    def test_returns_commits(self):
        commits = get_sample_commits()
        assert len(commits) > 0

    def test_commit_has_required_keys(self):
        required_keys = {'sha', 'message', 'author', 'date', 'url'}
        for commit in get_sample_commits():
            assert required_keys.issubset(commit.keys()), f"Commit missing keys: {commit}"

    def test_commit_values_are_strings(self):
        for commit in get_sample_commits():
            for key in ('sha', 'message', 'author', 'date', 'url'):
                assert isinstance(commit[key], str), f"commit['{key}'] should be a string"

    def test_commit_dates_are_formatted(self):
        for commit in get_sample_commits():
            assert len(commit['date']) == 10, f"Expected YYYY-MM-DD, got: {commit['date']}"
            assert commit['date'][4] == '-'
            assert commit['date'][7] == '-'


class TestGenerateReleaseNotes:
    def test_includes_header(self):
        result = generate_release_notes("- Feature A\n- Bug fix B", "2024-01-01", "owner/repo")
        assert "# Release Notes" in result

    def test_includes_repo_name(self):
        result = generate_release_notes("content", "2024-01-01", "owner/repo")
        assert "owner/repo" in result

    def test_includes_since_date(self):
        result = generate_release_notes("content", "2024-01-01", "owner/repo")
        assert "2024-01-01" in result

    def test_includes_ai_response(self):
        ai_response = "- Feature A\n- Bug fix B"
        result = generate_release_notes(ai_response, "2024-01-01", "owner/repo")
        assert ai_response in result

    def test_includes_review_disclaimer(self):
        result = generate_release_notes("content", "2024-01-01", "owner/repo")
        assert "review" in result.lower()

    def test_returns_string(self):
        result = generate_release_notes("content", "2024-01-01", "owner/repo")
        assert isinstance(result, str)

    def test_empty_ai_response(self):
        result = generate_release_notes("", "2024-01-01", "owner/repo")
        assert "# Release Notes" in result
        assert isinstance(result, str)


class TestFetchCommitsWithSampleData:
    def test_returns_sample_when_flag_set(self):
        commits = fetch_commits("any/repo", "2024-01-01", config={}, use_sample=True)
        assert commits == get_sample_commits()

    def test_sample_commit_count_matches(self):
        commits = fetch_commits("any/repo", "2024-01-01", config={}, use_sample=True)
        assert len(commits) == len(get_sample_commits())

    def test_sample_ignores_repo_argument(self):
        commits_a = fetch_commits("owner/repo-a", "2024-01-01", config={}, use_sample=True)
        commits_b = fetch_commits("owner/repo-b", "2024-01-01", config={}, use_sample=True)
        assert commits_a == commits_b
