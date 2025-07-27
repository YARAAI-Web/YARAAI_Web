rule auto_rule_20250726181801_0983 {
  strings:
    $o0 = "auxOutMessage" wide ascii nocase
    $o1 = "_onexit_lk" wide ascii nocase
    $o2 = "x12010u" wide ascii nocase
    $o3 = "dword_450EA4" wide ascii nocase
  condition:
    4 of ($o*)
}