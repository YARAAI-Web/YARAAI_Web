rule auto_rule_20250726125539_1753 {
  strings:
    $o0 = "dword_1400DD5A0" wide ascii nocase
    $o1 = "dword_1400DD5AC" wide ascii nocase
    $o2 = "dword_1400DD9EC" wide ascii nocase
    $o3 = "Mtx_init_in_situ" wide ascii nocase
  condition:
    4 of ($o*)
}