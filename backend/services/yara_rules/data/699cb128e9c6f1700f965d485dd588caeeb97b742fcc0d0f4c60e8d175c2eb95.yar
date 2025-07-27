rule auto_rule_20250726231023_4216 {
  strings:
    $o0 = "dword_457F08" wide ascii nocase
    $o1 = "cause" wide ascii nocase
    $o2 = "GetWsChanges" wide ascii nocase
    $o3 = "dword_458270" wide ascii nocase
  condition:
    4 of ($o*)
}