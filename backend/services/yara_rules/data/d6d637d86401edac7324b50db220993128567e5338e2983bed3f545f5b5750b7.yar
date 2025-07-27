rule auto_rule_20250726082921_7555 {
  strings:
    $o0 = "dword_46443C" wide ascii nocase
    $o1 = "dword_464294" wide ascii nocase
    $o2 = "dword_465468" wide ascii nocase
  condition:
    3 of ($o*)
}