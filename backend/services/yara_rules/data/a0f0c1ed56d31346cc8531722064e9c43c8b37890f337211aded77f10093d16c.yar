rule auto_rule_20250726122608_0797 {
  strings:
    $o0 = "dword_45FFB8" wide ascii nocase
    $o1 = "__sbh_alloc_new_group" wide ascii nocase
    $o2 = "dword_461794" wide ascii nocase
    $o3 = "dwInfoType" wide ascii nocase
  condition:
    4 of ($o*)
}