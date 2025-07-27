rule auto_rule_20250726190444_8906 {
  strings:
    $o0 = "_nh_malloc" wide ascii nocase
    $o1 = "dword_44C198" wide ascii nocase
    $o2 = "TrailDown2" wide ascii nocase
  condition:
    3 of ($o*)
}