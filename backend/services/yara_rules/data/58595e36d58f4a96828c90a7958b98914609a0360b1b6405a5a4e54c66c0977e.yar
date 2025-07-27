rule auto_rule_20250727040503_6961 {
  strings:
    $o0 = "dword_416F28" wide ascii nocase
    $o1 = "dword_455394" wide ascii nocase
  condition:
    all of them
}