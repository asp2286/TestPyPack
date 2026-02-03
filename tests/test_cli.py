from __future__ import annotations

from iitech_jfrog_demo.cli import main


def test_cli_output_contains_versions(capsys) -> None:
    main()
    captured = capsys.readouterr()
    output = captured.out
    assert "iitech-jfrog-multipypi-demo" in output
    assert "requests version" in output
    assert "pydantic version" in output
    assert "python-dateutil version" in output
    assert "rich version" in output
