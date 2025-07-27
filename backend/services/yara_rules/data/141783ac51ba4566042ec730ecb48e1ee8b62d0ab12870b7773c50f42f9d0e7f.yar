rule auto_rule_20250726143214_0138 {
  strings:
    $o0 = "dword_462CB8" wide ascii nocase
    $o1 = "copy_start" wide ascii nocase
    $o2 = "dword_463A18" wide ascii nocase
    $o3 = "__sbh_alloc_new_group" wide ascii nocase
    $o4 = "__sbh_resize_block" wide ascii nocase
  condition:
    4 of ($o*)
}