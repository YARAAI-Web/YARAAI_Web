rule auto_rule_20250726075331_9777 {
  strings:
    $o0 = "off_45C1CC" wide ascii nocase
    $o1 = "_heap_init" wide ascii nocase
    $o2 = "dword_45CF0C" wide ascii nocase
    $o3 = "__freetlocinfo" wide ascii nocase
  condition:
    4 of ($o*)
}