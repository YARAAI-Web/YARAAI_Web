rule auto_rule_20250726125402_9038 {
  strings:
    $o0 = "dword_1400DD70C" wide ascii nocase
    $o1 = "dword_1400DD830" wide ascii nocase
    $o2 = "dword_1400DD8A8" wide ascii nocase
  condition:
    3 of ($o*)
}