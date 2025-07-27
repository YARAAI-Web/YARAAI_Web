rule auto_rule_20250726060053_6873 {
  strings:
    $o0 = "old_esp" wide ascii nocase
    $o1 = "_nh_malloc" wide ascii nocase
    $o2 = "dword_411E68" wide ascii nocase
    $o3 = "_wincmdln" wide ascii nocase
  condition:
    4 of ($o*)
}