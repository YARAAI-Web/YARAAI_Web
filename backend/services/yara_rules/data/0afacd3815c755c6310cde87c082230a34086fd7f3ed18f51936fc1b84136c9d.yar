rule auto_rule_20250726061136_6543 {
  strings:
    $o0 = "__heap_select" wide ascii nocase
    $o1 = "_nh_malloc" wide ascii nocase
    $o2 = "dword_45CF0C" wide ascii nocase
    $o3 = "off_45C910" wide ascii nocase
    $o4 = "dword_45CB00" wide ascii nocase
  condition:
    4 of ($o*)
}