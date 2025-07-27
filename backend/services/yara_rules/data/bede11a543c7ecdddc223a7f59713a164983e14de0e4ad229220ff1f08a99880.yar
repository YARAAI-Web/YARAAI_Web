rule auto_rule_20250726211752_7796 {
  strings:
    $o0 = "_CrtDumpMemoryLeaks" wide ascii nocase
    $o1 = "Addend" wide ascii nocase
    $o2 = "IsBadWritePtr" wide ascii nocase
    $o3 = "TrailDown1_0" wide ascii nocase
  condition:
    4 of ($o*)
}