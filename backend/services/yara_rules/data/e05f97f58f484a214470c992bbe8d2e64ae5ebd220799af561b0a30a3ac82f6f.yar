rule auto_rule_20250726205314_0804 {
  strings:
    $o0 = "dword_783F4" wide ascii nocase
    $o1 = "__writecr0" wide ascii nocase
    $o2 = "ZwQueryValueKey" wide ascii nocase
  condition:
    3 of ($o*)
}