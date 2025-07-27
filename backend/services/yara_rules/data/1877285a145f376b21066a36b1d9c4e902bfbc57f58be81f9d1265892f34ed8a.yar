rule auto_rule_20250726191542_6670 {
  strings:
    $o0 = "_byte_0" wide ascii nocase
    $o1 = "dword_464424" wide ascii nocase
    $o2 = "TrailDown1" wide ascii nocase
    $o3 = "_nh_malloc_dbg" wide ascii nocase
  condition:
    4 of ($o*)
}