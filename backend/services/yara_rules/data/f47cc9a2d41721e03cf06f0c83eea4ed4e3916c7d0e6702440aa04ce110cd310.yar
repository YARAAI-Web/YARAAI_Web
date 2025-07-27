rule auto_rule_20250726081216_2973 {
  strings:
    $o0 = "dword_4336E4" wide ascii nocase
    $o1 = "dword_4347A0" wide ascii nocase
    $o2 = "aErrorLaunching" wide ascii nocase
  condition:
    3 of ($o*)
}