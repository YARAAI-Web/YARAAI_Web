rule auto_rule_20250726092208_2076 {
  strings:
    $o0 = "byte_4673C6" wide ascii nocase
    $o1 = "_CrtIsValidPointer" wide ascii nocase
    $o2 = "byte_467EE8" wide ascii nocase
    $o3 = "_output" wide ascii nocase
    $o4 = "should" wide ascii nocase
  condition:
    4 of ($o*)
}