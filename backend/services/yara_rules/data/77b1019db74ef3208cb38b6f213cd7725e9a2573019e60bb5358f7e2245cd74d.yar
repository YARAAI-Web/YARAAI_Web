rule auto_rule_20250727015157_0971 {
  strings:
    $o0 = "aCPcyosyvwfdgRc" wide ascii nocase
    $o1 = "off_416FFC" wide ascii nocase
    $o2 = "off_417E3C" wide ascii nocase
  condition:
    3 of ($o*)
}