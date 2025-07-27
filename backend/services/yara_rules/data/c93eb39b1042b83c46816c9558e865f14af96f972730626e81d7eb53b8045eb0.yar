rule auto_rule_20250726105656_7756 {
  strings:
    $o0 = "dword_7D50BD84" wide ascii nocase
    $o1 = "dynamic_atexit_destructor_for__no_snapshot_session___0" wide ascii nocase
  condition:
    all of them
}