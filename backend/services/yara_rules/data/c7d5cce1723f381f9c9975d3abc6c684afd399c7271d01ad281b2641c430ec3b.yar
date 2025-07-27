rule auto_rule_20250727025320_0797 {
  strings:
    $o0 = "nkrbtgt" wide ascii nocase
    $o1 = "RtlStringFromGUID" wide ascii nocase
    $o2 = "pbOutput" wide ascii nocase
  condition:
    3 of ($o*)
}