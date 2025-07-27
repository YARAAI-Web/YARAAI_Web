rule auto_rule_20250727012603_9683 {
  strings:
    $o0 = "byte_40DCA0" wide ascii nocase
    $o1 = "nProgram" wide ascii nocase
    $o2 = "_CrtIsValidPointer" wide ascii nocase
  condition:
    3 of ($o*)
}