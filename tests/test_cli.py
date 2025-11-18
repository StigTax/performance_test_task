from main import main


def test_main_prints_performance_report(cli_args_performance, capsys):
    main()

    captured = capsys.readouterr()
    out = captured.out

    assert "Backend" in out
    assert "5.00" in out
