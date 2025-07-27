rule auto_rule_20250726193135_4198 {
  strings:
    $o0 = "InterlockedIncrement" wide ascii nocase
    $o1 = "__initconin" wide ascii nocase
    $o2 = "_CrtIsValidPointer" wide ascii nocase
    $o3 = "_CrtDumpMemoryLeaks" wide ascii nocase
  condition:
    4 of ($o*)
}