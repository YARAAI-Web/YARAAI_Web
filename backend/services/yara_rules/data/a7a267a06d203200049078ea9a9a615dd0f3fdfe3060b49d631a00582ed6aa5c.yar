rule auto_rule_20250726105004_9079 {
  strings:
    $o0 = "ProcessorFeature" wide ascii nocase
    $o1 = "lpVersionInformation" wide ascii nocase
    $o2 = "x41000u" wide ascii nocase
    $o3 = "CreateIconFromResource" wide ascii nocase
  condition:
    4 of ($o*)
}